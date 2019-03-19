def sum_array(array):
    '''Return the sum of all items in an array.

    Argument:
        array (array): an array of numbers.

    Returns:
        int/float: the sum of all elements in array.

    Examples:
        >>> sum_array([1,2])
        3
        >>> sum_array([3,4,5])
        12
        >>> sum_array([6,7,8,9,10])
        40
    '''

    if len(array)==1:
        return array[0]
    else:
        return array[-1] + sum_array(array[0:-1])

def fibonacci(n):
    '''Return the nth term in the fibonacci sequence,
                    1,1,2,3,5,8,13,21,...

    Argument:
        n (int): nth term in fibonacci sequence to calculate.

    Returns:
        int: nth term of fibonacci sequence,
             equal to the sum of the previous two terms.

    Examples:
        >>> fibonacci(1)
        1
        >>> fibonacci(2)
        1
        >>> fibonacci(3)
        2
    '''
    
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def factorial(n):
    '''Return the factorial of n, denoted by n!, where
                n! = nx(n-1)x(n-2)x...x2x1

    Argument:
        n (int): the number whose factorial will be returned.

    Returns:
        int: the factorial of n.

    Examples:
            >>> factorial(1)
            1
            >>> factorial(2)
            2
            >>> factorial(3)
            6
    '''
    
    if n==0:
        return 1
    elif n==1:
        return n
    else:
        return n*factorial(n-1)

def reverse(word):
    '''Return word in reverse.

    Argument:
        word (string): a word.

    Returns:
        string: word in reverse.

    Examples:
        >>> reverse('abc')
        'cba'
        >>> reverse('word')
        'drow'
        >>> reverse('string')
        'gnirts'
    '''

    if len(word)==1:
        return word[0]
    else:
        return word[-1]+reverse(word[0:-1])
