from __future__ import annotations

from math import inf


class Graph:
    def __init__(self, directed: bool = False) -> None:
        self.directed = directed
        self.adj: dict[str, list[tuple[str, int]]] = {}

    def add_edge(self, u: str, v: str, w: int = 1) -> None:
        self.adj.setdefault(u, []).append((v, w))
        self.adj.setdefault(v, [])
        if not self.directed:
            self.adj[v].append((u, w))

    def bfs(self, start: str) -> list[str]:
        queue = [start]
        head = 0
        seen = {start}
        out: list[str] = []
        while head < len(queue):
            node = queue[head]
            head += 1
            out.append(node)
            for nxt, _ in self.adj[node]:
                if nxt not in seen:
                    seen.add(nxt)
                    queue.append(nxt)
        return out

    def dfs(self, start: str) -> list[str]:
        stack = [start]
        seen = set()
        out: list[str] = []
        while stack:
            node = stack.pop()
            if node in seen:
                continue
            seen.add(node)
            out.append(node)
            for nxt, _ in reversed(self.adj[node]):
                if nxt not in seen:
                    stack.append(nxt)
        return out

    def dijkstra(self, start: str) -> dict[str, int]:
        dist = {node: inf for node in self.adj}
        dist[start] = 0
        visited: set[str] = set()
        while len(visited) < len(self.adj):
            cur = None
            cur_d = inf
            for node, d in dist.items():
                if node not in visited and d < cur_d:
                    cur = node
                    cur_d = d
            if cur is None:
                break
            visited.add(cur)
            for nxt, w in self.adj[cur]:
                cand = dist[cur] + w
                if cand < dist[nxt]:
                    dist[nxt] = cand
        return {k: int(v) if v != inf else 10**9 for k, v in dist.items()}
