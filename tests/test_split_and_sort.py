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
    """Metamorphic test case: Scaling all integers by a positive factor."""
    input_list = [10, -9, 15, 7, 10, -5, 28]
    expected_output = ([-9, -5], [7, 10, 15, 28])
    result = split_and_sort(input_list)
    assert result == expected_output, f"Failed: Expected {expected_output}, got {result}"
    
    # Scale by factor 2
    input_list = [20, -18, 30, 14, 20, -10, 56]
    expected_output = ([-18, -10], [14, 20, 30, 56])
    result = split_and_sort(input_list)
    assert result == expected_output, f"Failed: Expected {expected_output}, got {result}"

def test_permutation_invariance():
    """Metamorphic test case: Check that permutation does not affect output."""
    input_list = [10, -9, 15, 7, 10, -5, 28]
    expected_output = ([-9, -5], [7, 10, 15, 28])
    result = split_and_sort(input_list)
    assert result == expected_output, f"Failed: Expected {expected_output}, got {result}"
    
    # Permuted version
    input_list = [15, 10, -5, 7, -9, 28, 10]
    expected_output = ([-9, -5], [7, 10, 15, 28])
    result = split_and_sort(input_list)
    assert result == expected_output, f"Failed: Expected {expected_output}, got {result}"

if __name__ == "__main__":
    pytest.main()