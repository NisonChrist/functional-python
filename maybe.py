from __future__ import annotations
from typing import Callable, TypeVar

T = TypeVar("T")
U = TypeVar("U")
V = TypeVar("V")


class Maybe[T]:
    def __init__(self, value: T | None):
        self._value: T | None = value

    def bind[U](self, fn: Callable[[T], Maybe[U]]) -> Maybe[U]:
        if self._value is None:
            return Maybe(None)
        else:
            return fn(self._value)

    @staticmethod
    def of[V](value: V) -> Maybe[V]:
        return Maybe(value)

    def apply[U](self, wrapped_fn: Maybe[Callable[[T], U]]) -> Maybe[U]:
        if self._value is None:
            return Maybe[U](None)
        if wrapped_fn._value is None:
            return Maybe[U](None)
        return Maybe(wrapped_fn._value(self._value))

    def __repr__(self):
        return f"Maybe({self._value})"


def safe_divide(x: int | float, y: int | float) -> Maybe[float | int]:
    if y == 0:
        return Maybe[float | int](None)
    else:
        return Maybe[float | int](x / y)


def square(x: int | float) -> int | float:
    return x * x


# Use Monad for chaining calls
result = Maybe[int](10).bind(lambda x: safe_divide(x, 2)).apply(Maybe(square))
print(result)  # Output: Maybe(25.0)

result = Maybe[int](10).bind(lambda x: safe_divide(x, 0)).apply(Maybe(square))
print(result)  # Output: Maybe(None)  Error automatically propagated
