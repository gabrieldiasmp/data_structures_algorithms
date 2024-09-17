import pytest
from bubble_sort import bubble_sort_algo

def test_bubble_sort_random_list():
    assert bubble_sort_algo([4, 2, 6, 5, 1, 3]) == [1, 2, 3, 4, 5, 6]

def test_bubble_sort_sorted_list():
    assert bubble_sort_algo([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]

def test_bubble_sort_duplicates():
    assert bubble_sort_algo([4, 4, 2, 6, 1, 3]) == [1, 2, 3, 4, 4, 6]

def test_bubble_sort_empty_list():
    assert bubble_sort_algo(["tst"]) == "ValueError: All elements in the list should be numbers (int or float)"

def test_bubble_sort_single_element():
    assert bubble_sort_algo([42]) == [42]

if __name__ == "__main__":
    pytest.main()