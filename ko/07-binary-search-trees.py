from __future__ import annotations


class BSTNode:
    def __init__(self, key: int) -> None:
        self.key = key
        self.left: BSTNode | None = None
        self.right: BSTNode | None = None


class BST:
    def __init__(self) -> None:
        self.root: BSTNode | None = None

    def insert(self, key: int) -> None:
        if self.root is None:
            self.root = BSTNode(key)
            return
        cur = self.root
        while True:
            if key < cur.key:
                if cur.left is None:
                    cur.left = BSTNode(key)
                    return
                cur = cur.left
            elif key > cur.key:
                if cur.right is None:
                    cur.right = BSTNode(key)
                    return
                cur = cur.right
            else:
                return

    def find(self, key: int) -> bool:
        cur = self.root
        while cur is not None:
            if key == cur.key:
                return True
            cur = cur.left if key < cur.key else cur.right
        return False

    def _delete(self, node: BSTNode | None, key: int) -> BSTNode | None:
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
            return node
        if key > node.key:
            node.right = self._delete(node.right, key)
            return node
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left
        succ = node.right
        while succ.left is not None:
            succ = succ.left
        node.key = succ.key
        node.right = self._delete(node.right, succ.key)
        return node

    def delete(self, key: int) -> None:
        self.root = self._delete(self.root, key)

    def inorder(self) -> list[int]:
        out: list[int] = []

        def walk(n: BSTNode | None) -> None:
            if n is None:
                return
            walk(n.left)
            out.append(n.key)
            walk(n.right)

        walk(self.root)
        return out

    def height(self) -> int:
        def h(node: BSTNode | None) -> int:
            if node is None:
                return -1
            return 1 + max(h(node.left), h(node.right))

        return h(self.root)
