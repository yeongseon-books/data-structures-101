from conftest import load_module


def test_heap_pop_order_and_heapsort():
    mod = load_module("ko/08-heaps.py")
    h = mod.MinHeap()
    values = [5, 1, 8, 2, 3]
    for v in values:
        h.push(v)
    popped = [h.pop() for _ in range(len(values))]
    assert popped == sorted(values)
    assert mod.heapsort(values) == sorted(values)
