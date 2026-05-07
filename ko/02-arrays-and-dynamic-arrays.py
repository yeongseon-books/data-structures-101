from __future__ import annotations


class DynamicArray:
    def __init__(self) -> None:
        self._capacity = 1
        self._size = 0
        self._data: list[int | None] = [None] * self._capacity
        self.resize_events = 0
        self.copy_ops = 0

    def __len__(self) -> int:
        return self._size

    @property
    def capacity(self) -> int:
        return self._capacity

    def _resize(self, new_capacity: int) -> None:
        new_data: list[int | None] = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
            self.copy_ops += 1
        self._data = new_data
        self._capacity = new_capacity
        self.resize_events += 1

    def append(self, value: int) -> None:
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        self._data[self._size] = value
        self._size += 1

    def pop(self) -> int:
        if self._size == 0:
            raise IndexError("pop from empty DynamicArray")
        self._size -= 1
        value = self._data[self._size]
        self._data[self._size] = None
        assert value is not None
        return int(value)

    def get(self, index: int) -> int:
        if not 0 <= index < self._size:
            raise IndexError(index)
        value = self._data[index]
        assert value is not None
        return int(value)

    def set(self, index: int, value: int) -> None:
        if not 0 <= index < self._size:
            raise IndexError(index)
        self._data[index] = value


if __name__ == "__main__":
    arr = DynamicArray()
    for n in range(16):
        arr.append(n)
    print(len(arr), arr.capacity, arr.resize_events)
