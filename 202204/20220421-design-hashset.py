"""
https://leetcode.com/problems/design-hashset/

HashSet: O(1) ideally, but can be O(n) on the worst case with hash collisions
"""


class MyHashSetEasy:
    def __init__(self):
        self.s = set()

    def add(self, key: int) -> None:
        self.s.add(key)

    def remove(self, key: int) -> None:
        try:
            self.s.remove(key)
        except KeyError:
            pass

    def contains(self, key: int) -> bool:
        return key in self.s


class MyHashSet:
    """
    Design a HashSet without using any built-in hash table libraries.

    개별 체이닝 방식 Hash Set 구현
    """
    def __init__(self):
        self.hash_length = 500
        self.final_list = [[] for _ in range(self.hash_length)]

    def add(self, key: int) -> None:
        search = key % self.hash_length
        if key in self.final_list[search]:
            return
        else:
            self.final_list[search].append(key)

    def remove(self, key: int) -> None:
        search = key % self.hash_length
        if key in self.final_list[search]:
            self.final_list[search].remove(key)

    def contains(self, key: int) -> bool:
        search = key % self.hash_length
        if key in self.final_list[search]:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
