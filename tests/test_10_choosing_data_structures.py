from conftest import load_module


def test_recommender_and_benchmark_shape():
    mod = load_module("ko/10-choosing-data-structures.py")
    ds, _ = mod.recommend_structure({"key_lookup": True})
    assert ds == "hash_table"
    ds, _ = mod.recommend_structure({"priority_pop": True})
    assert ds == "heap"
    result = mod.run_workload("dynamic_array", 200)
    assert result["ops"] > 0
