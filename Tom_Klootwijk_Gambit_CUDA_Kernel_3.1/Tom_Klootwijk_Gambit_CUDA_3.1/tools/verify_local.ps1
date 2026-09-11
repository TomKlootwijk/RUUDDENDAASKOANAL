$ErrorActionPreference = "Stop"
Set-Location (Join-Path $PSScriptRoot "..")
python tools/verify.py --hardware --sanitizers --profile @args
exit $LASTEXITCODE
