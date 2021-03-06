"""
https://leetcode.com/problems/implement-stack-using-queues/

> Follow-up: Can you implement the stack using only one queue?

[Similar Question]
https://leetcode.com/problems/implement-queue-using-stacks/

> Follow-up: Can you implement the queue such that each operation is amortized O(1) time complexity?
In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.
"""
from collections import deque


class MyStackRevised:
    """
    > Follow-up: Can you implement the stack using only one queue?
    """
    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        """
        시간 복잡도: O(n)

        queue: [1]
        queue: [1, 2] -> [2, 1]
        queue: [2, 1, 3] -> [3, 2, 1]
        queue: [3, 2, 1, 4] -> [4, 3, 2, 1]
        queue: [4, 3, 2, 1, 5] -> [5, 4, 3, 2, 1]

        # self.queue is "ALWAYS" ORDERED "LIFO" LIKE STACK

        [CONTRAST]: queue: [1, 2, 3, 4, 5] -> [5, 1, 2, 3, 4]
        """
        self.queue.append(x)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        """
        시간 복잡도: O(1)
        """
        return self.queue.popleft()

    def top(self) -> int:
        """
        시간 복잡도: O(1)
        """
        return self.queue[0]

    def empty(self) -> bool:
        """
        시간 복잡도: O(1)
        """
        return len(self.queue) == 0


class MyStackFirst:
    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        """
        시간 복잡도: O(1)
        """
        self.queue.append(x)

    def pop(self) -> int:
        """
        시간 복잡도: O(n)
        """
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

        return self.queue.popleft()

    def top(self) -> int:
        """
        시간 복잡도: O(n)
        """
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

        peeked = self.queue.popleft()
        self.queue.append(peeked)
        return peeked

    def empty(self) -> bool:
        """
        시간 복잡도: O(1)
        """
        return len(self.queue) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


class MyQueue:
    """
    > Follow-up: Can you implement the queue such that each operation is amortized O(1) time complexity?
    In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.
    """
    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def _convert_to_fifo_stack(self) -> None:
        if self.output_stack:
            return

        while self.input_stack:
            self.output_stack.append(self.input_stack.pop())

    def push(self, x: int) -> None:
        """
        시간 복잡도: O(1)
        """
        self.input_stack.append(x)

    def pop(self) -> int:
        """
        시간 복잡도: O(1) ~ O(n)
        """
        self._convert_to_fifo_stack()
        return self.output_stack.pop()

    def peek(self) -> int:
        """
        시간 복잡도: O(1) ~ O(n)
        """
        self._convert_to_fifo_stack()
        return self.output_stack[-1]

    def empty(self) -> bool:
        """
        시간 복잡도: O(1)
        """
        return 0 == len(self.input_stack) == len(self.output_stack)

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
