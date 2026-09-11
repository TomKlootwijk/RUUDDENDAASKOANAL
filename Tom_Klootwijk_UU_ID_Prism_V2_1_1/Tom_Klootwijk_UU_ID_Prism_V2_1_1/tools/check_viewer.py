#!/usr/bin/env python3
"""Optional offline Chromium checks for the shipped HTML viewer.

Requires Playwright and an independently installed Chromium executable. The exact
HTML is loaded with set_content, so the check does not require a local web server.
The output report goes to stdout; --capture optionally saves the initial view.
"""
from pathlib import Path
import argparse
import json
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--chromium', default=shutil.which('chromium') or shutil.which('chromium-browser'))
    parser.add_argument('--capture', type=Path, help='Optional destination for a fresh viewer screenshot')
    args = parser.parse_args()
    if not args.chromium:
        parser.error('Specify an installed Chromium executable with --chromium')
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print('Playwright is required for this optional check.', file=sys.stderr)
        return 1
    with sync_playwright() as automation:
        browser = automation.chromium.launch(executable_path=args.chromium, headless=True)
        page = browser.new_page(viewport={'width': 1365, 'height': 1500}, device_scale_factor=1.5)
        errors: list[str] = []
        requests: list[str] = []
        page.on('pageerror', lambda error: errors.append(str(error)))
        page.on('request', lambda request: requests.append(request.url))
        page.set_content((ROOT / 'app/index.html').read_text(encoding='utf-8'), wait_until='load')
        page.wait_for_timeout(200)
        assert page.locator('#facets tr').count() == 35
        assert '15' in page.locator('#summary').inner_text()
        if args.capture:
            args.capture.parent.mkdir(parents=True, exist_ok=True)
            box = page.locator('.columns').bounding_box()
            if box is None:
                raise ValueError('Viewer cards were not laid out')
            page.screenshot(path=str(args.capture), clip={'x': 0, 'y': 0, 'width': 1365,
                                                          'height': box['y'] + box['height'] + 8})
        page.locator('#preview').click()
        assert 'PRIVATE VIEW' in page.locator('#meta').inner_text()
        assert page.locator('#save').is_disabled()
        page.locator('#preview').click()
        page.locator('#step').click()
        assert '0' in page.locator('#summary').inner_text()
        page.locator('#file').set_input_files(str(ROOT / 'verification/demo/snapshot.json'))
        page.wait_for_timeout(100)
        assert 'LOCAL FILE' in page.locator('#viewMode').inner_text()
        page.locator('#replay').click()
        page.wait_for_timeout(100)
        page.locator('#replay').click()
        assert page.locator('#replay').inner_text() == 'Replay synthetic updates'
        external = [url for url in requests if url.startswith(('http:', 'https:'))]
        assert not errors, errors
        assert not external, external
        print(json.dumps({'renderer': 'Chromium / Playwright',
                          'load_mode': 'exact shipped HTML via set_content',
                          'facet_rows': 35, 'import_view': 'passed', 'private_view': 'passed',
                          'replay_controls': 'passed', 'javascript_errors': errors,
                          'external_network_requests': external}, indent=2))
        browser.close()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
