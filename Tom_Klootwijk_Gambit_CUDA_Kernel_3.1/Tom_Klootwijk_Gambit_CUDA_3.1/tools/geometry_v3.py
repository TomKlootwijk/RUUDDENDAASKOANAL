"""Seed, growth, field, coding and recurrent-state reference implementation.

All coordinates are simulation units unless an API explicitly specifies metres
or seconds. Composite fields preserve set membership; they are not advertised
as globally exact signed distances. No hardware or biomedical output is used.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Callable, Iterable
import hashlib
import json
import math
import numpy as np

VERSION = "3.0.0"
RULES = {"X": "X[+X]Y", "Y": "Y[-Y]X", "[": "[", "]": "]", "+": "+", "-": "-"}
SWAP = str.maketrans({"X": "Y", "Y": "X", "+": "-", "-": "+"})


def finite_array(value, *, last_dim: int | None = None) -> np.ndarray:
    a = np.asarray(value, dtype=float)
    if not np.all(np.isfinite(a)):
        raise ValueError("All values must be finite")
    if last_dim is not None and (a.ndim == 0 or a.shape[-1] != last_dim):
        raise ValueError(f"Expected final dimension {last_dim}")
    return a


def finite_scalar(value: float, name: str) -> float:
    x = float(value)
    if not math.isfinite(x):
        raise ValueError(f"{name} must be finite")
    return x


@dataclass(frozen=True)
class Pair:
    """Ordered symbolic pair; X and Y are tokens, not a person classifier."""
    first: str
    second: str

    def __post_init__(self):
        if self.first not in {"X", "Y"} or self.second not in {"X", "Y"}:
            raise ValueError("Pair symbols must be X or Y")

    @classmethod
    def parse(cls, text: str) -> "Pair":
        if not isinstance(text, str) or len(text) != 2:
            raise ValueError("A pair must be a two-character string")
        return cls(text[0], text[1])

    @property
    def word(self) -> str:
        return self.first + self.second

    @property
    def canonical(self) -> str:
        return "".join(sorted(self.word))

    @property
    def parity(self) -> int:
        return int(self.first != self.second)

    @property
    def axiom(self) -> str:
        return f"[{self.first}][{self.second}]"


def mix_pairs(a: Pair, b: Pair) -> dict[str, Fraction]:
    """Exact formal one-token-from-each mixing law: four equiprobable draws."""
    out: dict[str, Fraction] = {}
    for x in a.word:
        for y in b.word:
            k = Pair(x, y).canonical
            out[k] = out.get(k, Fraction(0)) + Fraction(1, 4)
    return dict(sorted(out.items()))


def rewrite(word: str, max_symbols: int = 200_000) -> str:
    if any(x not in RULES for x in word):
        raise ValueError("Unknown grammar token")
    new_size = sum(len(RULES[x]) for x in word)
    if new_size > max_symbols:
        raise ValueError("Growth exceeds the configured symbol budget")
    return "".join(RULES[x] for x in word)


def grow(pair: Pair, generations: int, max_symbols: int = 200_000) -> str:
    if not isinstance(generations, int) or isinstance(generations, bool) or generations < 0:
        raise ValueError("generations must be a nonnegative integer")
    if max_symbols < len(pair.axiom):
        raise ValueError("Budget is smaller than the axiom")
    word = pair.axiom
    for _ in range(generations):
        word = rewrite(word, max_symbols)
    return word


def swap_word(word: str) -> str:
    if any(x not in RULES for x in word):
        raise ValueError("Unknown grammar token")
    return word.translate(SWAP)


def turtle(word: str, step: float = 0.12, angle: float = math.pi / 7,
           shrink: float = 0.72) -> np.ndarray:
    """Interpret X/Y as forward strokes; brackets save/restore full state."""
    if step <= 0 or not (0 < shrink <= 1):
        raise ValueError("step > 0 and 0 < shrink <= 1 are required")
    for x, name in [(step, "step"), (angle, "angle"), (shrink, "shrink")]:
        finite_scalar(x, name)
    pos = np.zeros(2); heading = math.pi / 2
    stack: list[tuple[np.ndarray, float]] = []; segments = []
    for token in word:
        if token in "XY":
            nxt = pos + step * shrink ** len(stack) * np.array([math.cos(heading), math.sin(heading)])
            segments.append(np.stack([pos.copy(), nxt.copy()])); pos = nxt
        elif token == "+": heading += angle
        elif token == "-": heading -= angle
        elif token == "[": stack.append((pos.copy(), heading))
        elif token == "]":
            if not stack: raise ValueError("Unbalanced closing bracket")
            pos, heading = stack.pop()
        else: raise ValueError("Unknown turtle token")
    if stack: raise ValueError("Unbalanced opening bracket")
    return np.asarray(segments, dtype=float).reshape(-1, 2, 2)


def distance_segment(points, a, b) -> np.ndarray:
    p = finite_array(points, last_dim=2)
    a = finite_array(a, last_dim=2); b = finite_array(b, last_dim=2)
    if a.shape != (2,) or b.shape != (2,):
        raise ValueError("Segment endpoints must be two-vectors")
    v = b - a; den = float(np.dot(v, v))
    if den == 0: return np.linalg.norm(p-a, axis=-1)
    t = np.clip(np.sum((p-a)*v, axis=-1) / den, 0.0, 1.0)
    return np.linalg.norm(p - a - t[..., None]*v, axis=-1)


def distance_arc(points, radius: float = 1.0, aperture: float = math.pi/2) -> np.ndarray:
    """Exact unsigned distance to R(sin theta, cos theta), |theta| <= aperture."""
    radius = finite_scalar(radius, "radius"); aperture = finite_scalar(aperture, "aperture")
    if radius <= 0 or not 0 < aperture <= math.pi/2:
        raise ValueError("radius > 0 and 0 < aperture <= pi/2 required")
    p = finite_array(points, last_dim=2).copy(); p[..., 0] = np.abs(p[..., 0])
    sc = np.array([math.sin(aperture), math.cos(aperture)])
    endpoint = np.linalg.norm(p - radius*sc, axis=-1)
    radial = np.abs(np.linalg.norm(p, axis=-1) - radius)
    return np.where(sc[1]*p[...,0] > sc[0]*p[...,1], endpoint, radial)


def paired_arcs(points, radius: float = 1.0, spacing: float = 1.0,
                thickness: float = 0.08, aperture: float = math.pi/2,
                folded: bool = False) -> np.ndarray:
    p = finite_array(points, last_dim=2)
    spacing = finite_scalar(spacing, "spacing"); thickness = finite_scalar(thickness, "thickness")
    if spacing < 0 or thickness <= 0: raise ValueError("spacing >= 0 and thickness > 0 required")
    if folded:
        q = p.copy(); q[...,0] = np.abs(q[...,0]) - spacing
        return distance_arc(q, radius, aperture) - thickness
    off = np.array([spacing, 0.0])
    return np.minimum(distance_arc(p-off, radius, aperture),
                      distance_arc(p+off, radius, aperture)) - thickness


def m_field(points, radius: float = 1.0, spacing: float = 1.0,
            thickness: float = 0.08, aperture: float = math.pi/2,
            baseline: bool = True, clipped: bool = True) -> np.ndarray:
    """Explicit two-arc union, optional baseline and y>=0 clipping.

    Uses the explicit union, not the conditionally valid fold shortcut.
    The returned field is 1-Lipschitz and sign-correct, not generally an exact SDF.
    """
    p = finite_array(points, last_dim=2)
    phi = paired_arcs(p, radius, spacing, thickness, aperture)
    if baseline:
        phi = np.minimum(phi, distance_segment(p, [-spacing-radius,0], [spacing+radius,0]) - thickness)
    if clipped: phi = np.maximum(phi, -p[...,1])
    return phi


def capsule_field(points, segments, thickness: float = 0.03) -> np.ndarray:
    p = finite_array(points, last_dim=2); s = finite_array(segments)
    if s.ndim != 3 or s.shape[1:] != (2,2) or len(s) == 0:
        raise ValueError("segments must be nonempty with shape (N,2,2)")
    if not math.isfinite(thickness) or thickness <= 0: raise ValueError("thickness > 0 required")
    out = np.full(p.shape[:-1], np.inf)
    for a,b in s: out = np.minimum(out, distance_segment(p,a,b)-thickness)
    return out

