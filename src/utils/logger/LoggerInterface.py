from typing import Any, Protocol
from collections.abc import Sequence


class LoggerInterface(Protocol):
    def debug(message: str, *args: Sequence[Any]) -> None: ...

    def info(message: str, *args: Sequence[Any]) -> None: ...

    def warn(message: str, *args: Sequence[Any]) -> None: ...

    def error(message: str, *args: Sequence[Any]) -> None: ...
