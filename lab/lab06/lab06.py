## List Mutation ##
def map(fn, lst):
    """Maps fn onto lst using mutation.
    >>> original_list = [5, -1, 2, 0]
    >>> map(lambda x: x * x, original_list)
    >>> original_list
    [25, 1, 4, 0]
    """
    "*** YOUR CODE HERE ***"
    i = 0
    for x in lst:
        lst[i] = fn(x)
        i += 1

def filter(pred, lst):
    """Filters lst with pred using mutation.
    >>> original_list = [5, -1, 2, 0]
    >>> filter(lambda x: x % 2 == 0, original_list)
    >>> original_list
    [2, 0]
    """
    "*** YOUR CODE HERE ***"
    """i = 0
    while i != len(lst):
        if not pred(lst[i]):
            lst.pop(i)
            i -= 1
        i += 1"""
    #new=[]
    #return [new.append(x) for x in lst if pred(x)]
    return [x for x in lst if pred(x)]






## Dictionaries ##

def replace_all(d, x, y):
    """Replace all occurrences of x as a value (not a key) in d with y.
    >>> d = {3: '3', 'foo': 2, 'bar': 3, 'garply': 3, 'xyzzy': 99}
    >>> replace_all(d, 3, 'poof')
    >>> d == {3: '3', 'foo': 2, 'bar': 'poof', 'garply': 'poof', 'xyzzy': 99}
    True
    """
    "*** YOUR CODE HERE ***"
    for key in d:
        if d[key] == x:
            d[key] = y
