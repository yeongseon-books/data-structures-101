from conftest import load_module


def test_tree_traversals_and_metrics():
    mod = load_module("ko/06-trees.py")
    root = mod.TreeNode(1)
    n2 = root.add(mod.TreeNode(2))
    n3 = root.add(mod.TreeNode(3))
    n2.add(mod.TreeNode(4))
    n2.add(mod.TreeNode(5))
    n3.add(mod.TreeNode(6))
    assert mod.preorder(root) == [1, 2, 4, 5, 3, 6]
    assert mod.postorder(root) == [4, 5, 2, 6, 3, 1]
    assert mod.levelorder(root) == [1, 2, 3, 4, 5, 6]
    assert mod.size(root) == 6
    assert mod.depth(root) == 2
