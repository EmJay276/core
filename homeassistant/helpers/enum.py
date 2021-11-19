"""Enum related helpers."""

from typing import Any

try:
    # pylint: disable=unused-import # to be imported from here
    from enum import StrEnum  # type: ignore[attr-defined]
except ImportError:
    from enum import Enum

    class StrEnum(str, Enum):  # type: ignore[no-redef]
        """Partial backport of Python 3.11's StrEnum for our basic use cases."""

        def __new__(cls, value: str, *args: Any, **kwargs: Any) -> "StrEnum":
            """Create a new StrEnum instance."""
            # enum.auto intentionally not backported yet, waiting until it's
            # very clear that its implementation will no longer change.
            if not isinstance(value, str):
                raise TypeError(f"{value!r} is not a string")
            return super().__new__(cls, value, *args, **kwargs)  # type: ignore[call-overload]

        def __str__(self) -> str:
            """Return self.value."""
            return str(self.value)
