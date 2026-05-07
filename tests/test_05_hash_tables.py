from conftest import load_module


def test_hash_table_lookup_and_collision_count():
    mod = load_module("ko/05-hash-tables.py")
    table = mod.HashTableChaining(capacity=4)
    k1 = mod.BadKey(1)
    k2 = mod.BadKey(2)
    table.put(k1, "x")
    table.put(k2, "y")
    assert table.get(k1) == "x"
    assert table.collisions > 0
