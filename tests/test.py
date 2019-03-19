from PackageName import myFunction

def test_sum_array():
    """
    make sure sum_array works correctly
    """

    assert myFunction.sum_array([1,2,3]) == 6, 'incorrect'
    assert myFunction.sum_array([2,2]) == 4, 'incorrect'
    assert myFunction.sum_array([6,7,8,9,10]) == 40, 'incorrect'

def test_fibonacci():
    """
    make sure fibonacci works correctly
    """

    assert myFunction.fibonacci(1) == 1, 'incorrect'
    assert myFunction.fibonacci(2) == 1, 'incorrect'
    assert myFunction.fibonacci(4) == 3, 'incorrect'

def test_factorial():
    """
    make sure factorial works correctly
    """

    assert myFunction.factorial(1) == 1, 'incorrect'
    assert myFunction.factorial(2) == 2, 'incorrect'
    assert myFunction.factorial(4) == 24, 'incorrect'

def reverse():
    """
    make sure reverse works correctly
    """

    assert myFunction.reverse('word') == 'drow', 'incorrect'
    assert myFunction.reverse('string') == 'gnirts', 'incorrect'
    assert myFunction.reverse('abcdefg') == 'gfedcba', 'incorrect'

def bubble_sort():
    """
    make sure bubble_sort works correctly
    """

    assert myFunction.bubble_sort([1,2,3]) == [1,2,3], 'incorrect'
    assert myFunction.bubble_sort([3,2,1]) == [1,2,3], 'incorrect'
    assert myFunction.bubble_sort([5,3,8,1,4]) == [1,3,4,5,8], 'incorrect'

def merge_sort():
    """
    make sure merge_sort works correctly
    """

    assert myFunction.merge_sort([1,2,3]) == [1,2,3], 'incorrect'
    assert myFunction.merge_sort([3,2,1]) == [1,2,3], 'incorrect'
    assert myFunction.merge_sort([5,3,8,1,4]) == [1,3,4,5,8], 'incorrect'

def quick_sort():
    """
    make sure quick_sort works correctly
    """

    assert myFunction.quick_sort([1,2,3]) == [1,2,3], 'incorrect'
    assert myFunction.quick_sort([3,2,1]) == [1,2,3], 'incorrect'
    assert myFunction.quick_sort([5,3,8,1,4]) == [1,3,4,5,8], 'incorrect'
