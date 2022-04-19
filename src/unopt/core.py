"""Core module of unopt."""

from typing import cast, Callable, Optional, TypeVar

T = TypeVar("T")


class UnwrapError(ValueError):
    """Error class to indicage invalid unwrapping."""

    pass


def unwrap(obj: Optional[T]) -> T:
    """Unwrap Optional[T].

    Args:
        `obj`: An object to be unwrapped.

    Returns:
        `obj` itself if it is not `None`.

    Raises:
        `UnwrapError`: `obj` is `None`.
    """
    if obj is None:
        raise UnwrapError
    return obj


def unwrap_or(obj: Optional[T], default: T) -> T:
    """Unwraps Optional[T] or returns a default value.

    Args:
        `obj`: An object to be unwrapped.
        `default`: Default value returned when `obj` is `None`.

    Returns:
        `obj` itself if it is not `None`, `default` otherwise.
    """
    return obj if obj is not None else default


def unwrap_or_else(obj: Optional[T], default_fn: Callable[[], T]) -> T:
    """Unwraps Optional[T] or returns a default value obtained by a function.

    Args:
        `obj`: An object to be unwrapped.
        `default_fn`: A function to provide a default value.

    Returns:
        `obj` itself if it is not `None`, `default_fn()` otherwise.
        `default_fn` is not called if `obj` is not `None`.
    """
    return obj if obj is not None else default_fn()


def unwrap_unchecked(obj: Optional[T]) -> T:
    """Unwrap Optional[T] without value checking.

    Args:
        `obj`: An object to be unwrapped.

    Returns:
        `obj` itself regardless of the underlying value.
    """
    return cast(T, obj)
