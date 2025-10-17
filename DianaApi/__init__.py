"""User-friendly entry point for the Diana robot Python SDK.

`import DianaApi` exposes all low-level bindings defined in `DianaApi.DianaApi`.
"""

from . import DianaApi as api

__all__ = ["api"]


def __getattr__(name):
    """Fallback to attributes defined in the low-level API module."""
    if hasattr(api, name):
        return getattr(api, name)
    raise AttributeError(f"module 'DianaApi' has no attribute '{name}'")
