"""
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
"""
from typing import List
from collections import namedtuple

CharCntPair = namedtuple('CharCntPair', 'char cnt')


class CharCntPairs:
    def __init__(self, char: str, cnt: int):
        self.char = char
        self.cnt = cnt


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        """
        시간 복잡도: O(n)
        공간 복잡도: O(n)
        """
        char_stack: List[CharCntPairs] = []

        for char in s:
            if char_stack and char_stack[-1].char == char:
                char_stack[-1].cnt += 1
            else:
                char_stack.append(CharCntPairs(char, 1))

            if char_stack[-1].cnt == k:  # eager
                char_stack.pop()

        return ''.join(char_cnt_pair.char * char_cnt_pair.cnt for char_cnt_pair in char_stack)

    def removeDuplicatesWithMultiplePop(self, s: str, k: int) -> str:
        """
        시간 복잡도: O(n) - all the characters on the input string can be popped at most once!
        공간 복잡도: O(n)
        """
        char_stack: List[CharCntPair] = []

        for char in s:
            if char_stack and char_stack[-1].char == char:
                char_stack.append(CharCntPair(char, char_stack[-1].cnt + 1))
            else:
                char_stack.append(CharCntPair(char, 1))

            if char_stack[-1].cnt == k:  # eager
                for _ in range(k):
                    char_stack.pop()

        return ''.join(char for char, _ in char_stack)

    def removeDuplicatesWithLinkedList(self, s: str, k: int) -> str:
        """
        Time Limit Exceeded
        """
        cur_node = dummy_head = CharNode()

        for char in s:
            prev_node = cur_node
            cur_node = CharNode(char=char, prev_node=prev_node)
            prev_node.next = cur_node

        has_chance_to_remove = True

        while has_chance_to_remove:
            remove_start_node = node = dummy_head.next
            cur_char, cur_cumul_cnt = None, 0

            has_chance_to_remove = False

            while node:
                if cur_char != node.char:
                    cur_char = node.char
                    cur_cumul_cnt = 1
                    remove_start_node = node
                else:
                    cur_cumul_cnt += 1
                    if cur_cumul_cnt == k:
                        has_chance_to_remove = True
                        # print('[start]', remove_start_node)
                        # print('[end]', node)
                        if node.next:
                            remove_start_node.prev.next, node.next.prev = node.next, remove_start_node.prev
                        else:
                            remove_start_node.prev.next = None

                        remove_start_node = node.next
                        cur_cumul_cnt = 0

                node = node.next

        res_char_list = []
        res_node = dummy_head.next
        while res_node:
            res_char_list.append(res_node.char)
            res_node = res_node.next

        return ''.join(res_char_list)


class CharNode:
    def __init__(
        self, char: str = None, prev_node: 'CharNode' = None, next_node: 'CharNode' = None
    ):
        self.char = char
        self.prev = prev_node
        self.next = next_node

    def __str__(self) -> str:
        return f'{self.char} | prev: {self.prev and self.prev.char} | next: {self.next and self.next.char}'


if __name__ == '__main__':
    sol = Solution()
    print(sol.removeDuplicates("yfttttfbbbbnnnnffbgffffgbbbbgssssgthyyyy", 4))
    print(sol.removeDuplicatesWithMultiplePop("yfttttfbbbbnnnnffbgffffgbbbbgssssgthyyyy", 4))
