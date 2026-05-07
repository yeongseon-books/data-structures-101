from conftest import load_module


def test_singly_and_doubly_linked_lists():
    mod = load_module("ko/03-linked-lists.py")
    sll = mod.SinglyLinkedList()
    for v in [1, 2, 3]:
        sll.insert_tail(v)
    assert sll.find(2)
    assert sll.remove(2)
    sll.reverse()
    assert sll.to_list() == [3, 1]

    dll = mod.DoublyLinkedList()
    for v in [1, 2, 3]:
        dll.insert_tail(v)
    assert dll.remove(2)
    dll.reverse()
    assert dll.to_list() == [3, 1]
