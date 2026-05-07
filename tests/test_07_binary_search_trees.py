from conftest import load_module


def test_bst_inorder_and_delete():
    mod = load_module("ko/07-binary-search-trees.py")
    bst = mod.BST()
    values = [5, 3, 7, 2, 4, 6, 8]
    for v in values:
        bst.insert(v)
    assert bst.inorder() == sorted(values)
    bst.delete(7)
    assert not bst.find(7)
    assert bst.inorder() == [2, 3, 4, 5, 6, 8]
