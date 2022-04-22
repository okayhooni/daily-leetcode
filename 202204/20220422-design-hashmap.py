"""
https://leetcode.com/problems/design-hashmap/

HashMap: O(1) ideally, but can be O(n) on the worst case with hash collisions
"""
from typing import List, Tuple


class MyHashMap:
    """
    Design a HashMap without using any built-in hash table libraries.

    개별 체이닝 방식 Hash Map 구현
    """
    def __init__(self):
        self.hash_length = 500
        self.hash_buckets: List[List[Tuple[int]]] = [[] for _ in range(self.hash_length)]

    def _get_hash_key(self, key):
        return key % self.hash_length

    def put(self, key: int, value: int) -> None:
        search_key = self._get_hash_key(key)
        for idx, (k, v) in enumerate(self.hash_buckets[search_key]):
            if key == k:
                target_idx_on_chain = idx
                break
        else:
            target_idx_on_chain = None

        if target_idx_on_chain is None:
            self.hash_buckets[search_key].append((key, value))
        else:
            self.hash_buckets[search_key][target_idx_on_chain] = (key, value)

    def get(self, key: int) -> int:
        search_key = self._get_hash_key(key)
        for k, v in self.hash_buckets[search_key]:
            if key == k:
                return v
        else:
            return -1

    def remove(self, key: int) -> None:
        search_key = self._get_hash_key(key)
        for idx, (k, v) in enumerate(self.hash_buckets[search_key]):
            if key == k:
                target_idx_on_chain = idx
                break
        else:
            target_idx_on_chain = None

        if target_idx_on_chain is not None:
            self.hash_buckets[search_key].pop(target_idx_on_chain)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
