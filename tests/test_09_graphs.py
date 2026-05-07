from conftest import load_module


def test_graph_bfs_dfs_dijkstra():
    mod = load_module("ko/09-graphs.py")
    g = mod.Graph(directed=False)
    edges = [
        ("A", "B", 1),
        ("A", "C", 4),
        ("B", "C", 2),
        ("B", "D", 5),
        ("C", "D", 1),
    ]
    for u, v, w in edges:
        g.add_edge(u, v, w)
    assert g.bfs("A") == ["A", "B", "C", "D"]
    assert g.dfs("A")[0] == "A"
    assert g.dijkstra("A") == {"A": 0, "B": 1, "C": 3, "D": 4}
