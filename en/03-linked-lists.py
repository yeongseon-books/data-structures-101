from __future__ import annotations


class Node:
    def __init__(
        self, value: int, next: "Node | None" = None, prev: "Node | None" = None
    ) -> None:
        self.value = value
        self.next = next
        self.prev = prev


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None
        self.size = 0

    def insert_head(self, value: int) -> None:
        node = Node(value=value, next=self.head)
        self.head = node
        if self.tail is None:
            self.tail = node
        self.size += 1

    def insert_tail(self, value: int) -> None:
        node = Node(value=value)
        if self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def find(self, value: int) -> bool:
        cur = self.head
        while cur is not None:
            if cur.value == value:
                return True
            cur = cur.next
        return False

    def remove(self, value: int) -> bool:
        prev = None
        cur = self.head
        while cur is not None:
            if cur.value == value:
                if prev is None:
                    self.head = cur.next
                else:
                    prev.next = cur.next
                if self.tail is cur:
                    self.tail = prev
                self.size -= 1
                return True
            prev, cur = cur, cur.next
        return False

    def reverse(self) -> None:
        prev = None
        cur = self.head
        self.tail = self.head
        while cur is not None:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def to_list(self) -> list[int]:
        cur = self.head
        out: list[int] = []
        while cur is not None:
            out.append(int(cur.value))
            cur = cur.next
        return out


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None

    def insert_head(self, value: int) -> None:
        node = Node(value=value, next=self.head)
        if self.head is not None:
            self.head.prev = node
        else:
            self.tail = node
        self.head = node

    def insert_tail(self, value: int) -> None:
        node = Node(value=value, prev=self.tail)
        if self.tail is not None:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node

    def remove(self, value: int) -> bool:
        cur = self.head
        while cur is not None:
            if cur.value == value:
                if cur.prev:
                    cur.prev.next = cur.next
                else:
                    self.head = cur.next
                if cur.next:
                    cur.next.prev = cur.prev
                else:
                    self.tail = cur.prev
                return True
            cur = cur.next
        return False

    def find(self, value: int) -> bool:
        cur = self.head
        while cur is not None:
            if cur.value == value:
                return True
            cur = cur.next
        return False

    def reverse(self) -> None:
        cur = self.head
        self.head, self.tail = self.tail, self.head
        while cur is not None:
            cur.prev, cur.next = cur.next, cur.prev
            cur = cur.prev

    def to_list(self) -> list[int]:
        out: list[int] = []
        cur = self.head
        while cur is not None:
            out.append(int(cur.value))
            cur = cur.next
        return out
