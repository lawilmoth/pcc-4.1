import assignment
from cpo import *

#4.1
def test_loop_over_list():
    
    captured = capture_print_output(assignment.loop_over_list)()

    assert captured == "apple\nbanana\ncarrot\ndate"

#4.2
def test_loop_over_list_and_capitalize():
    captured = capture_print_output(
        assignment.loop_over_list_and_capitalize
        )()
    assert captured == "0: Apple\n1: Banana\n2: Carrot\n3: Date"
    captured = capture_print_output(
        assignment.loop_over_list_and_capitalize
        )()
    
#4.3
def test_print_numbers_1_to_10():
    
    captured = capture_print_output(
        assignment.print_numbers_1_to_10
        )()
    assert captured == "1\n2\n3\n4\n5\n6\n7\n8\n9\n10"

#4.4
def test_print_numbers_1_to_n():
    captured = capture_print_output(
        assignment.print_numbers_1_to_n
        )()
    assert captured == "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15"

    

#4.5
def test_create_list_of_numbers():
    assert assignment.create_list_of_numbers(5) == [1, 2, 3, 4, 5]
    assert assignment.create_list_of_numbers(10) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#4.6
def test_create_list_of_even_numbers():
    assert assignment.create_list_of_even_numbers(10) == [2, 4, 6, 8, 10]
    assert assignment.create_list_of_even_numbers(20) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

#4.7
def test_create_list_of_first_ten_cube_numbers():
    assert assignment.create_list_of_first_ten_cube_numbers() == [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

#4.8
def test_create_list_comprehension_of_first_ten_cube_numbers():
    assert assignment.create_list_comprehension_of_first_ten_cube_numbers() == [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

#4.9
def test_copy_list_and_append_11():
    original_list = [1, 2, 3, 4, 5]
    new_list = assignment.copy_list_and_append_11(original_list)
    assert new_list == [1, 2, 3, 4, 5, 11]
    assert original_list == [1, 2, 3, 4, 5]

    original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    new_list = assignment.copy_list_and_append_11(original_list)
    assert new_list == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    assert original_list == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#4.10
def test_return_first_index_of_tuple():
    assert assignment.return_first_index_of_tuple((1, 2, 3)) == 1

    assert assignment.return_first_index_of_tuple((2, 3, 4, 5)) == 2

#4.11
def test_loop_over_tuple():


    captured = capture_print_output(assignment.loop_over_tuple)()
    assert captured == "1\n2\n3\n4\n5"

