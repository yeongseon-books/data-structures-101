from __future__ import annotations


def recommend_structure(profile: dict[str, object]) -> tuple[str, str]:
    random_access = bool(profile.get("random_access", False))
    frequent_insert = bool(profile.get("frequent_insert", False))
    key_lookup = bool(profile.get("key_lookup", False))
    priority_pop = bool(profile.get("priority_pop", False))
    ordered_scan = bool(profile.get("ordered_scan", False))

    if priority_pop:
        return "heap", "최솟값/최댓값 우선 꺼내기가 핵심이라 힙이 적합합니다."
    if key_lookup:
        return "hash_table", "키 기반 조회가 많아서 해시 테이블이 유리합니다."
    if random_access and not frequent_insert:
        return "dynamic_array", "임의 접근이 빈번하고 삽입 이동 비용이 낮습니다."
    if frequent_insert and not random_access:
        return "linked_list", "중간 삽입/삭제가 많고 순차 접근 위주입니다."
    if ordered_scan:
        return "bst", "정렬 순회가 중요해서 BST 계열이 유리합니다."
    return "dynamic_array", "기본 선택으로 단순한 동적 배열이 가장 실용적입니다."


def run_workload(structure: str, n: int = 1000) -> dict[str, int]:
    ops = 0
    if structure == "dynamic_array":
        data: list[int] = []
        for i in range(n):
            data.append(i)
            ops += 1
        for i in range(0, n, 10):
            _ = data[i]
            ops += 1
    elif structure == "linked_list":

        class Node:
            def __init__(self, value: int, next: "Node | None" = None) -> None:
                self.value = value
                self.next = next

        head = None
        for i in range(n):
            head = Node(i, next=head)
            ops += 1
        cur = head
        while cur is not None:
            cur = cur.next
            ops += 1
    elif structure == "hash_table":
        buckets: list[list[tuple[int, int]]] = [[] for _ in range(128)]
        for i in range(n):
            idx = i % 128
            buckets[idx].append((i, i))
            ops += 1
        for i in range(0, n, 10):
            idx = i % 128
            for k, _ in buckets[idx]:
                ops += 1
                if k == i:
                    break
    return {"ops": ops}
