from conftest import load_module


def test_dynamic_array_amortized_copy_ops():
    mod = load_module("ko/02-arrays-and-dynamic-arrays.py")
    arr = mod.DynamicArray()
    n = 1024
    for i in range(n):
        arr.append(i)
    assert len(arr) == n
    assert arr.copy_ops < 2 * n
    assert arr.get(100) == 100
