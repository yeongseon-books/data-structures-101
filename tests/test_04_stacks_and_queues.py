from conftest import load_module


def test_stack_queue_and_use_cases():
    mod = load_module("ko/04-stacks-and-queues.py")
    s = mod.ArrayStack()
    s.push("a")
    s.push("b")
    assert s.pop() == "b"

    q = mod.ArrayQueue()
    q.enqueue("a")
    q.enqueue("b")
    assert q.dequeue() == "a"
    assert mod.is_balanced_parentheses("({[]})")
    assert not mod.is_balanced_parentheses("([)]")
    graph = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
    assert mod.bfs_order(graph, "A") == ["A", "B", "C", "D"]
