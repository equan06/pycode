import pytest
from dll import DLL, DLLNode

def test_dll_append():
    dll = DLL()
    lst = [1, 2, 3, 4, 5]
    for l in lst:
        dll.append(DLLNode(l))

    assert str(dll) == str(lst)

def test_dll_remove():
    dll = DLL()
    node1 = DLLNode(1)
    node2 = DLLNode(2)
    node3 = DLLNode(3)

    dll.append(node1)
    dll.append(node2)
    dll.append(node3)

    dll.remove(node2)

    assert str(dll) == str([1, 3])

    dll.remove(node1)
    assert str(dll) == str([3])

    dll.remove(node3)
    assert str(dll) == str([])