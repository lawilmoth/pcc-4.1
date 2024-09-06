import pytest
import  assignment
import pytest
import assignment

def test_return_first_element():
    lst = [1, 2, 3, 4, 5]
    assert assignment.return_first_element(lst) == 1
    lst = [5, 4, 3, 2, 1]
    assert assignment.return_first_element(lst) == 5

def test_return_last_element():
    lst = [1, 2, 3, 4, 5]
    assert assignment.return_last_element(lst) == 5
    lst = [5, 4, 3, 2, 1]
    assert assignment.return_last_element(lst) == 1

def test_add_element_to_an_fstring():
    lst = ["hello", "world"]
    assert assignment.add_element_to_a_string(lst) == "The first element of the list is: Hello"
    lst = ["mr.", "Wilmoth", "Rocks"]
    assert assignment.add_element_to_a_string(lst) == "The first element of the list is: Mr."


def test_change_the_first_element():
    lst = [1, 2, 3, 4, 5]
    assert assignment.change_the_first_element(lst) == ["Python", 2, 3, 4, 5]

def test_change_the_last_element():
    lst = [1, 2, 3, 4, 5]
    assert assignment.change_the_last_element(lst) == [1, 2, 3, 4, "Spam"]

def test_add_element_to_the_end():
    lst = [1, 2, 3, 4, 5]
    assert assignment.add_element_to_the_end(lst) == [1, 2, 3, 4, 5, "Eggs"]

def test_add_element_to_the_beginning():
    lst = [1, 2, 3, 4, 5]
    assert assignment.add_element_to_the_beginning(lst) == ["Eggs", 0, 1, 2, 3, 4, 5]

def test_remove_last_element():
    lst = [1, 2, 3, 4, 5]
    assert assignment.remove_last_element(lst) == [1, 2, 3, 4]

def test_remove_first_element():
    lst = [1, 2, 3, 4, 5]
    new_lst, removed_element = assignment.remove_first_element(lst)
    assert new_lst == [2, 3, 4, 5]
    assert removed_element == 1

def test_remove_element_at_index():
    lst = [1, 2, 3, 4, 5]
    assert assignment.remove_element_at_index(lst, 2) == [1, 2, 4, 5]

def test_insert_element_at_index():
    lst = [1, 2, 3, 4, 5]
    assert assignment.insert_element_at_index(lst, 2, 10) == [1, 2, 10, 3, 4, 5]

def test_remove_element_by_value():
    lst = [1, 2, 3, 4, 5]
    assert assignment.remove_element_by_value(lst, 3) == [1, 2, 4, 5]

def test_sort_list_alphabetically():
    lst = ["banana", "apple", "cherry", "date"]
    assert assignment.sort_list_alphabetically(lst) == ["apple", "banana", "cherry", "date"]

def test_reverse_list():
    lst = [1, 2, 3, 4, 5]
    assert assignment.reverse_list(lst) == [5, 4, 3, 2, 1]
