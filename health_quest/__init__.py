"""Health Quest — ethics-first food-literacy game.

This module exposes the version and the transparent scoring weights used by
the browser app so research users can import the model, not just open the
HTML.
"""
from __future__ import annotations

__version__ = "3.1.0"

HEALTH_SCORE_WEIGHTS = {
    "sugar": "higher sugar lowers the score",
    "salt": "higher sodium lowers the score",
    "protein": "adequate protein supports a higher score",
    "fibre": "adequate fibre supports a higher score",
}

__all__ = ["__version__", "HEALTH_SCORE_WEIGHTS"]