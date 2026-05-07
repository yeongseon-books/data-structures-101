from conftest import load_module


def test_duplicate_strategies_agree():
    mod = load_module("ko/01-what-are-data-structures.py")
    values = [1, 2, 3, 2, 4, 5, 1, 1]
    result = mod.run_demo(values)
    expected = [1, 2]
    assert sorted(result["quadratic"][0]) == expected
    assert sorted(result["sorted"][0]) == expected
    assert sorted(result["hash"][0]) == expected
