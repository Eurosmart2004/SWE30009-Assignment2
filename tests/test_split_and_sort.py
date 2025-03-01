from assignment2 import split_and_sort
import pytest

def test_only_single_sign_integers():
    """Test cases where input contains only positive or only negative numbers."""
    # Scenario A: Only positive integers
    input_list = [13, 7, 9, 15]
    expected_output = ([], [7, 9, 13, 15])
    result = split_and_sort(input_list)
    assert result == expected_output, f"Failed: Expected {expected_output}, got {result}"
    
    # Scenario B: Only negative integers
    input_list = [-13, -7, -9, -15]
    expected_output = ([-15, -13, -9, -7], [])
    result = split_and_sort(input_list)
    assert result == expected_output, f"Failed: Expected {expected_output}, got {result}"

def test_mixed_integers_with_zero():
    """Test case with both positive and negative integers, including zero."""
    input_list = [0, -1, 1, -2, 2]
    expected_output = ([-2, -1, 0], [1, 2])
    result = split_and_sort(input_list)
    assert result == expected_output, f"Failed: Expected {expected_output}, got {result}"

def test_duplicated_integers():
    """Test case with duplicate integers."""
    input_list = [12, -8, 14, 6, 12, -4, 26, 0]
    expected_output = ([-8, -4, 0], [6, 12, 14, 26])
    result = split_and_sort(input_list)
    assert result == expected_output, f"Failed: Expected {expected_output}, got {result}"

def test_maximum_length_input():
    """Test case with exactly 30 elements to check upper limit."""
    input_list = [-15, -15, -10, -9, -8, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    expected_output = ([-15, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
    result = split_and_sort(input_list)
    assert result == expected_output, f"Failed: Expected {expected_output}, got {result}"

def test_scaling_by_positive_factor():
    """Metamorphic test case: Scaling all integers by a positive factor should maintain order and uniqueness."""
    
    si = [10, -9, 15, 7, -5, 28]
    so = split_and_sort(si)
    
    # Step 2: Scale input by a factor of 2
    factor = 2
    fi = [x * factor for x in si]
    fo = split_and_sort(fi)
    
    # Step 3: Expected transformed output
    expected_fo = ([x * factor for x in so[0]], [x * factor for x in so[1]])

    # Step 4: Assertion
    assert fo == expected_fo, f"Failed: Expected {expected_fo}, got {fo}"


def test_permutation_invariance():
    """Metamorphic test case: Check that permutation does not affect output."""
    
    # Step 1: Original input and expected output
    si = [10, -9, 15, 7, -5, 28]
    so = split_and_sort(si)
    
    # Step 2: Permute input
    fi = [15, 10, -5, 7, -9, 28]
    fo = split_and_sort(fi)
    
    # Step 3: Assertion (order in output should be the same as original)
    assert fo == so, f"Failed: Expected {so}, got {fo}"


if __name__ == "__main__":
    pytest.main()