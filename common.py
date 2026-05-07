from __future__ import annotations

from dataclasses import dataclass
from time import perf_counter
from typing import Any, Callable


@dataclass
class Node:
    value: Any
    next: Any = None
    prev: Any = None


class OperationCounter:
    def __init__(self) -> None:
        self.counts: dict[str, int] = {}

    def inc(self, key: str, amount: int = 1) -> None:
        self.counts[key] = self.counts.get(key, 0) + amount

    def get(self, key: str) -> int:
        return self.counts.get(key, 0)

    def total(self) -> int:
        return sum(self.counts.values())


def time_op(fn: Callable[[], Any]) -> tuple[Any, float]:
    start = perf_counter()
    value = fn()
    return value, perf_counter() - start
