from hw2_debugging import merge_sort

def test_merge_sort_1():
    # Test for a single element in an array
    input_arr = [9]
    result = merge_sort(input_arr)
    expected = [9]
    assert result == expected, f"Expected {expected}, but got {result}"

def test_merge_sort_2():
    # Test for an empty array
    input_arr = []
    result = merge_sort(input_arr)
    expected = []
    assert result == expected, f"Expected {expected}, but got {result}"

def test_merge_sort_3():
    # Test for decreasing array 
    input_arr = [8, 6, 5, 3, 1, 0]
    result = merge_sort(input_arr)
    expected = [0, 1, 3, 5, 6, 8]
    assert result == expected, f"Expected {expected}, but got {result}"

def test_merge_sort_4():
    # Test for increasing array 
    input_arr = [0, 1, 3, 5, 20]
    result = merge_sort(input_arr)
    expected = [0, 1, 3, 5, 20]
    assert result == expected, f"Expected {expected}, but got {result}"

def test_merge_sort_5():
    # Test for random elements in an array 
    input_arr = [20, 9, 11, 14, 5, 16, 7, 15, 1, 17, 10, 18, 8, 3, 19, 18, 14, 18, 7, 4]
    result = merge_sort(input_arr)
    expected = [1, 3, 4, 5, 7, 7, 8, 9, 10, 11, 14, 14, 15, 16, 17, 18, 18, 18, 19, 20]
    assert result == expected, f"Expected {expected}, but got {result}"

def test_merge_sort_6():
    # Test for random elements in an array 
    input_arr = [5, 5, 5, 5, 5]
    result = merge_sort(input_arr)
    expected = [5, 5, 5, 5, 5]
    assert result == expected, f"Expected {expected}, but got {result}"

