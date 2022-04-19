# unopt: Utility functions to unwrap `Optional[T]`

## Overview

*unopt* provides several utility functions to "unwrap" the `Optional[T]` (or `T | None`)
objects: removes the `Optional` type hint and obtains the underlying object.

*unopt* functions are inspired by the Rust's `Option<T>` functionality, but the behavior
is tuned to Python's convention. E.g., `unwrap()` raises an exception instead of
aborting.

## Examples

```python
from unopt import *

foo: Optional[int] = 123
bar: Optional[int] = None

# unwrap() returns the given object if it is not None.
assert unwrap(foo) == 123
unwrap(bar)  # Raises UnwrapError

# unwrap_or() returns the default value if the given object is None.
assert unwrap_or(foo, 456) == 123
assert unwrap_or(bar, 456) == 456

# unwrap_or_else() returns the default value obtained by invoking the given function.
assert unwrap_or_else(foo, lambda: 456) == 123
assert unwrap_or_else(bar, lambda: 456) == 456

# unwrap_unchecked() just casts the given object without value checking.
assert unwrap_unchecked(foo) == 123
assert unwrap_unchecked(bar) is None  # Unsafe
```