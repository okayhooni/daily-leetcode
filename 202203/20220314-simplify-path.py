"""
https://leetcode.com/problems/simplify-path
"""


class Solution:
    """
    시간 복잡도: O(n)
    공간 복잡도: O(n)
    """
    def simplifyPath(self, path: str) -> str:
        path_elements = path.split('/')
        path_stack = []

        for e in path_elements:
            if not e or e == '.':
                continue

            if e == '..':
                try:
                    path_stack.pop()
                except IndexError:
                    pass
            else:
                path_stack.append(e)

        return '/' + '/'.join(path_stack)
