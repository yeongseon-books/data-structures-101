from __future__ import annotations


class HashTableChaining:
    def __init__(self, capacity: int = 8) -> None:
        self.capacity = capacity
        self.buckets: list[list[tuple[object, object]]] = [[] for _ in range(capacity)]
        self.size = 0
        self.collisions = 0

    def _index(self, key: object) -> int:
        return hash(key) % self.capacity

    def put(self, key: object, value: object) -> None:
        idx = self._index(key)
        bucket = self.buckets[idx]
        if bucket:
            self.collisions += 1
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self.size += 1

    def get(self, key: object) -> object:
        for k, v in self.buckets[self._index(key)]:
            if k == key:
                return v
        raise KeyError(key)


class HashTableOpenAddressing:
    EMPTY = object()
    DELETED = object()

    def __init__(self, capacity: int = 8) -> None:
        self.capacity = capacity
        self.slots: list[object] = [self.EMPTY] * capacity
        self.size = 0
        self.collisions = 0

    def _find_slot(self, key: object) -> int:
        start = hash(key) % self.capacity
        idx = start
        while True:
            slot = self.slots[idx]
            if slot is self.EMPTY or slot is self.DELETED:
                return idx
            if isinstance(slot, tuple) and slot[0] == key:
                return idx
            self.collisions += 1
            idx = (idx + 1) % self.capacity
            if idx == start:
                raise RuntimeError("table full")

    def put(self, key: object, value: object) -> None:
        idx = self._find_slot(key)
        if self.slots[idx] is self.EMPTY or self.slots[idx] is self.DELETED:
            self.size += 1
        self.slots[idx] = (key, value)

    def get(self, key: object) -> object:
        start = hash(key) % self.capacity
        idx = start
        while True:
            slot = self.slots[idx]
            if slot is self.EMPTY:
                break
            if isinstance(slot, tuple) and slot[0] == key:
                return slot[1]
            idx = (idx + 1) % self.capacity
            if idx == start:
                break
        raise KeyError(key)


class BadKey:
    def __init__(self, value: int) -> None:
        self.value = value

    def __hash__(self) -> int:
        return 1

    def __eq__(self, other: object) -> bool:
        return isinstance(other, BadKey) and self.value == other.value
