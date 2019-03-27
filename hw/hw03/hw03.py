HW_SOURCE_FILE = 'hw03.py'

#############
# Questions #
#############

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
        return n
    else:
        return g(n-1) + 2 * g(n-2) + 3 * g(n-3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    "*** YOUR CODE HERE ***"
    a , b, c = 1, 2, 3
    if n <= 3:
        return n
    else:
        for i in range (1, n - 2):
            total = c + 2*b + 3*a
            c, b, a = total, c, b
        return total



def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    "*** YOUR CODE HERE ***"
    i = 0
    n = k
    while k >= 1:
        k = k // 10
        i = i + 1

    while i > 0:
        if n % 10 == 7:
            return True
        else:
            n = n // 10
            i = i - 1
    return False




def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    def condition(t):
        if t == 1:
            return True
        elif has_seven(t-1) or (t-1) % 7 == 0:
            return not condition(t-1)
        else:
            return condition(t-1)
    if n == 1:
        return 1
    elif n == 2:
        return 2

    else:
        if condition(n):
            return pingpong(n-1) + 1
        else:
            return pingpong(n-1) - 1

def max_power(n):
    i = n
    while n >= 2:
        if n % 2 == 0:
            n = n // 2
        else:
            i = i - 1
            n = i
    return i


def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    "*** YOUR CODE HERE ***"
    n = max_power(amount)
    def inner(amount, n):
        if amount == 0:
            return 1
        elif amount < 0:
            return 0
        elif amount == 1:
            return 1
        elif n == 1:
            return 1
        else:
            with_n = inner(amount-n, n)
            without_n = inner(amount, n//2)
        return with_n + without_n
    return inner(amount, n)



def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"
    mid = 6 - start - end
    if n == 1:
        print_move(start, end)
    else:
        move_stack(n-1, start, mid)
        move_stack(1, start, end)
        move_stack(n-1, mid, end)


def flatten(lst):
    """Returns a flattened version of lst.

    >>> flatten([1, 2, 3])     # normal list
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      # deep list
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    """
    "*** YOUR CODE HERE ***"
    lst1 = []
    for i in range (0, len(lst)):
        element = lst[i]
        if type(element) == list:
            for t in range (0, len(element)):
                element1 = element[t]
                if type(element1) == list:
                    lst1 += flatten(element1)
                else:
                    lst1 += element[t:t+1]
        else:
            lst1 += lst[i:i+1]
    return lst1


def merge(lst1, lst2):
    """Merges two sorted lists.

    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    "*** YOUR CODE HERE ***"
    lst3 = lst1 + lst2
    for i in range (0, len(lst3) - 1):
        for t in range (0, len(lst3) - 1):
            if lst3[t] > lst3[t+1]:
                lst3[t], lst3[t+1] = lst3[t+1], lst3[t]
    return lst3

def mergesort(seq):
    """Mergesort algorithm.

    >>> mergesort([4, 2, 5, 2, 1])
    [1, 2, 2, 4, 5]
    >>> mergesort([])     # sorting an empty list
    []
    >>> mergesort([1])   # sorting a one-element list
    [1]
    """
    "*** YOUR CODE HERE ***"
    return merge(seq, [])
