"""
https://leetcode.com/problems/flatten-nested-list-iterator/
"""


class NestedInteger:
    """
    This is the interface that allows for creating nested lists.
    You should not implement it, or speculate about its implementation
    """

    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """

    def getList(self) -> ['NestedInteger']:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """


class ListIdxPair:
    def __init__(self, nested_list: [NestedInteger], next_index: int = 0):
        self.nested_list = nested_list
        self.next_index = next_index

    def __repr__(self) -> str:
        return f'ListIdxPair(next_idx:{self.next_index})'


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nested_list_stack = [ListIdxPair(nested_list=nestedList)]
        self.tmp_next = None

    def _internal_next(self):
        if self.tmp_next is not None:
            return self.tmp_next

        next_element = None

        while next_element is None:
            try:
                list_idx_pair = self.nested_list_stack[-1]
            except IndexError:
                return

            try:
                next_element = list_idx_pair.nested_list[list_idx_pair.next_index]
            except IndexError:
                self.nested_list_stack.pop()
            finally:
                list_idx_pair.next_index += 1

        if next_element.isInteger():
            return next_element.getInteger()
        else:
            self.nested_list_stack.append(ListIdxPair(nested_list=next_element.getList()))
            return self._internal_next()

    def next(self) -> int:
        res = self._internal_next()
        self.tmp_next = None
        return res

    def hasNext(self) -> bool:
        self.tmp_next = self._internal_next()
        return self.tmp_next is not None


class NestedGenerator:
    def __init__(self, nestedList: [NestedInteger]):
        self.generator = self._make_generator(nestedList)
        self._peeked = None

    def _make_generator(self, nestedList: [NestedInteger]):
        for nested in nestedList:
            if nested.isInteger():
                yield nested.getInteger()
            else:
                yield from self._make_generator(nested.getList())

    def next(self) -> int:
        if self._peeked is not None:
            res, self._peeked = self._peeked, None
        else:
            res = next(self.generator)

        return res

    def hasNext(self) -> bool:
        if self._peeked is not None:
            return True

        try:
            self._peeked = next(self.generator)
        except StopIteration:
            return False
        else:
            return True


class NestedIterator52msSol:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack: [NestedInteger] = []

        for nestedInt in nestedList:
            self.stack.append(nestedInt)

        self.stack.reverse()

    def _makeStackTopAnInteger(self):
        while self.stack and not self.stack[-1].isInteger():
            nestedInt: NestedInteger = self.stack.pop(-1)

            nestedList = nestedInt.getList()
            nestedListLength = len(nestedList)

            for i in range(nestedListLength - 1, -1, -1):
                self.stack.append(nestedList[i])

    def next(self) -> int:
        self._makeStackTopAnInteger()

        if self.stack:
            topInt: NestedInteger = self.stack.pop(-1)
            return topInt.getInteger()

        return None

    def hasNext(self) -> bool:
        self._makeStackTopAnInteger()

        return self.stack

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
