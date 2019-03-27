# Q1
class ScaleIterator:
    """An iterator the scales elements of the iterable s by a number k.

    >>> s = ScaleIterator([1, 5, 2], 5)
    >>> for elem in s:
    ...     print(elem)
    5
    25
    10
    >>> m = ScaleIterator([1, 2, 3, 4, 5, 6], 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    def __init__(self, s, k):
        self.index = 0
        self.s = s
        self.k = k

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.s):
            raise StopIteration
        result = self.s[self.index] * self.k
        self.index += 1
        return result
