"""Package definition of unopt."""

from unopt import core

UnwrapError = core.UnwrapError

unwrap = core.unwrap
unwrap_or = core.unwrap_or
unwrap_or_else = core.unwrap_or_else
unwrap_unchecked = core.unwrap_unchecked

__all__ = [
    "UnwrapError",
    "unwrap",
    "unwrap_or",
    "unwrap_or_else",
    "unwrap_unchecked",
]
