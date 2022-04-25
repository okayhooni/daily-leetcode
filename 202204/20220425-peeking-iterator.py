"""
https://leetcode.com/problems/peeking-iterator/

> Follow up: How would you extend your design to be generic and work with all types, not just integer?
"""


# Below is the interface for Iterator, which is already defined for you.
class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """


class PeekingIterator:
    def __init__(self, iterator: Iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.tmp_next = self.iterator.next()

    def peek(self) -> int:
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.tmp_next

    def next(self) -> int:
        """
        :rtype: int
        """
        res = self.tmp_next
        tmp_next = self.iterator.next()
        if 1 <= tmp_next <= 1000:
            self.tmp_next = tmp_next
        else:
            self.tmp_next = None

        return res

    def hasNext(self) -> bool:
        """
        :rtype: bool
        """
        return self.tmp_next is not None


class PeekingIteratorWithUsingHasNext:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.peek_val = None
        self._iterator = iterator

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.peek_val:
            return self.peek_val

        self.peek_val = self._iterator.next()
        return self.peek_val

    def next(self):
        """
        :rtype: int
        """
        if self.peek_val:
            res = self.peek_val
            self.peek_val = None
            return res
        return self._iterator.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.peek_val:
            return True
        return self._iterator.hasNext()

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
