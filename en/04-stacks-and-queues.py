from __future__ import annotations


class Node:
    def __init__(self, value: str, next: "Node | None" = None) -> None:
        self.value = value
        self.next = next


class ArrayStack:
    def __init__(self, capacity: int = 4) -> None:
        self._data: list[object | None] = [None] * capacity
        self._size = 0

    def _grow(self) -> None:
        new: list[object | None] = [None] * (len(self._data) * 2)
        for i in range(self._size):
            new[i] = self._data[i]
        self._data = new

    def push(self, value: str) -> None:
        if self._size == len(self._data):
            self._grow()
        self._data[self._size] = value
        self._size += 1

    def pop(self) -> str:
        if self._size == 0:
            raise IndexError("pop from empty stack")
        self._size -= 1
        value = self._data[self._size]
        self._data[self._size] = None
        assert value is not None
        return str(value)


class LinkedListStack:
    def __init__(self) -> None:
        self._head: Node | None = None

    def push(self, value: str) -> None:
        self._head = Node(value=value, next=self._head)

    def pop(self) -> str:
        if self._head is None:
            raise IndexError("pop from empty stack")
        value = self._head.value
        self._head = self._head.next
        return str(value)


class ArrayQueue:
    def __init__(self, capacity: int = 4) -> None:
        self._data: list[object | None] = [None] * capacity
        self._front = 0
        self._size = 0

    def _grow(self) -> None:
        new: list[object | None] = [None] * (len(self._data) * 2)
        for i in range(self._size):
            new[i] = self._data[(self._front + i) % len(self._data)]
        self._data = new
        self._front = 0

    def enqueue(self, value: str) -> None:
        if self._size == len(self._data):
            self._grow()
        idx = (self._front + self._size) % len(self._data)
        self._data[idx] = value
        self._size += 1

    def dequeue(self) -> str:
        if self._size == 0:
            raise IndexError("dequeue from empty queue")
        value = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        assert value is not None
        return str(value)


class LinkedListQueue:
    def __init__(self) -> None:
        self._head: Node | None = None
        self._tail: Node | None = None

    def enqueue(self, value: str) -> None:
        node = Node(value=value)
        if self._tail is None:
            self._head = self._tail = node
        else:
            self._tail.next = node
            self._tail = node

    def dequeue(self) -> str:
        if self._head is None:
            raise IndexError("dequeue from empty queue")
        value = self._head.value
        self._head = self._head.next
        if self._head is None:
            self._tail = None
        return str(value)


def is_balanced_parentheses(expr: str) -> bool:
    pairs = {")": "(", "]": "[", "}": "{"}
    opens = set(pairs.values())
    stack = ArrayStack()
    for ch in expr:
        if ch in opens:
            stack.push(ch)
        elif ch in pairs:
            try:
                if stack.pop() != pairs[ch]:
                    return False
            except IndexError:
                return False
    return stack._size == 0


def bfs_order(graph: dict[str, list[str]], start: str) -> list[str]:
    queue = ArrayQueue()
    queue.enqueue(start)
    seen = {start}
    out: list[str] = []
    while queue._size:
        node = queue.dequeue()
        out.append(node)
        for nxt in graph.get(node, []):
            if nxt not in seen:
                seen.add(nxt)
                queue.enqueue(nxt)
    return out
