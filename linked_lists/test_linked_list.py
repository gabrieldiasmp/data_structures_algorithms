import pytest
from linked_list import LinkedListAlgo

def test_simple_insert():
    # First example
    my_linked_list = LinkedListAlgo(4)

    assert my_linked_list.head.value == 4
    assert my_linked_list.tail.value == 4
    assert my_linked_list.length == 1

def test_append_linked_list():
    # Second example: append
    my_linked_list = LinkedListAlgo(1)
    my_linked_list.append(2)
    my_linked_list.append(3)
    my_linked_list.append(15)
    my_linked_list.append(47)

    assert my_linked_list.length == 5
    assert my_linked_list.tail.value == 47
    assert my_linked_list.head.value == 1


def test_get_linked_list():
    # Second example: append
    my_linked_list = LinkedListAlgo(1)
    my_linked_list.append(2)
    my_linked_list.append(3)
    my_linked_list.append(15)
    my_linked_list.append(47)

    assert my_linked_list.get(4).value == 47

def test_pop_linked_list():
    my_linked_list = LinkedListAlgo(1)
    my_linked_list.append(2)
    my_linked_list.append(3)
    my_linked_list.append(15)
    my_linked_list.append(47)
    
    my_linked_list.pop()
    assert my_linked_list.tail.value == 15

def test_popfirst_linked_list():
    my_linked_list = LinkedListAlgo(1)
    my_linked_list.append(2)
    my_linked_list.append(3)
    my_linked_list.append(15)
    my_linked_list.append(47)
    
    my_linked_list.pop_first()
    assert my_linked_list.head.value == 2

def test_set_value_linked_list():
    my_linked_list = LinkedListAlgo(1)
    my_linked_list.append(2)
    my_linked_list.append(3)
    my_linked_list.append(15)
    my_linked_list.append(47)

    my_linked_list.set_value(index=3, new_value=54)

    assert my_linked_list.get(3).value == 54


    


if __name__ == "__main__":
    pytest.main()