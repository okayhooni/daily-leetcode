"""
https://leetcode.com/problems/search-suggestions-system/

> Topic: Trie / Design / String / Binary Search

Hint 1) Brute force is a good choice because length of the string is ≤ 1000.
Hint 2) Binary search the answer.
Hint 3) Use Trie data structure to store the best three matching. Traverse the Trie.

Ref) https://dev.to/seanpgallivan/solution-search-suggestions-system-90e

Despite the fact that the clues suggest a binary search and a trie,
the optimal solution to this problem needs neither.
The substrings formed by adding one letter at a time from the search word (S),
are naturally already in lexicographical order,
as are the results that we're instructed to push into our answer array (ans).

So if we sort the products array (P), we should only ever need to iterate through P,
once during the entire remaining process of the solution with a time complexity of O(N).
A single binary search would only require log(N) time, but we'd have to perform M = S.length binary searches,
so in total they would take O(M * log(N)) time, compared to the O(N) time of a simple iteration.

With constraints of 1000 on both M and N,
the binary search route would max out at a worse time complexity than iteration.
Regardless, the sort itself, which is required for both, requires O(N * log(N)) time already,
so neither option can decrease the overall time complexity required.

So in order to only require a single pass through P,
we should keep track of the current bounds for the range of matches (left, right),
then we'll iterate through the characters (c) of S.
At each iteration,
we'll first want to move left forward and right back to narrow the range of matches based on the new value of c.
"""
from typing import List, Dict
from dataclasses import dataclass, field
from bisect import bisect_left, bisect_right


@dataclass
class TrieNode:
    char: str = None
    product_idx: List[int] = field(default_factory=list)
    next_node_by_char: Dict[str, "TrieNode"] = field(default_factory=dict)


class ProductRecommender:
    def __init__(self, products: List[str]):
        self.products = sorted(products)
        self.trie_root = TrieNode()
        self._make_trie()

    def _make_trie(self):
        for product_idx, product_name in enumerate(self.products):
            cur_node = self.trie_root

            for char in product_name:
                if char not in cur_node.next_node_by_char:
                    cur_node.next_node_by_char[char] = TrieNode(char)

                cur_node = cur_node.next_node_by_char[char]
                cur_node.product_idx.append(product_idx)

    def recommend_from_seq_input(self, search_word: str, max_suggestions: int = 3) -> List[List[str]]:
        cur_node = self.trie_root
        suggestions = []
        for char_idx, char in enumerate(search_word):
            try:
                cur_node = cur_node.next_node_by_char[char]
            except KeyError:
                cur_node = TrieNode()
                suggestions.append([])
            else:
                suggestions.append([
                    self.products[product_idx]
                    for product_idx in cur_node.product_idx[:max_suggestions]
                ])

        return suggestions


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        """
        Time Complexity: O(N * log(N)) where N is the length of P / for sorting
        (extra) Space Complexity: O(N)
        """
        recommender = ProductRecommender(products)
        return recommender.recommend_from_seq_input(searchWord)

    def suggestedProductsRef(self, products: List[str], searchWord: str) -> List[List[str]]:
        """
        Time Complexity: O(N * log(N)) where N is the length of P / for sorting
        (extra) Space Complexity: O(1) excluding output space required for ans / in-place sorting trick on argument
        """
        products.sort()
        ans = []
        left, right = 0, len(products) - 1

        for i in range(len(searchWord)):
            # c, res = searchWord[i], []
            c = searchWord[i]
            while left <= right and (len(products[left]) == i or products[left][i] < c):
                left += 1
            while left <= right and (len(products[right]) == i or products[right][i] > c):
                right -= 1
            # for j in range(3):
            #     if left + j > right:
            #         break
            #     else:
            #         res.append(products[left + j])
            # ans.append(res)
            ans.append(products[left:min(left + 3, right + 1)])
        return ans

    def suggestedProductsWithBinarySearch(self, products: List[str], searchWord: str) -> List[List[str]]:
        """
        Time Complexity: O(N * log(N)) where N is the length of P / for sorting
        (extra) Space Complexity: O(1) excluding output space required for ans / in-place sorting trick on argument
        """
        products.sort()
        ans = []
        left, right = 0, len(products)

        for i in range(len(searchWord)):
            c = searchWord[i]
            # near_right_c = chr(ord(c) + 1)
            cur_target = [p[i:i+1] for p in products[left:right]]
            # right = left + bisect_left(cur_target, near_right_c)
            right = left + bisect_right(cur_target, c)
            left += bisect_left(cur_target, c)

            ans.append(products[left:min(left + 3, right)])
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.suggestedProductsWithBinarySearch(
        # products=["mobile", "mouse", "moneypot", "monitor", "mousepad"],
        # searchWord="mouse"
        products=["bags", "baggage", "banner", "box", "cloths"],
        searchWord="bags"
    ))
