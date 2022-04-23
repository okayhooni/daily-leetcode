"""
https://leetcode.com/problems/encode-and-decode-tinyurl/
"""
from typing import List, Dict
from random import choices
from itertools import chain


class Codec:
    """
    same longUrl can be encoded different shortUrl on multiple times.
    """
    VALID_CHR_ORDS: List[int] = list(chain(
        range(ord('0'), ord('9') + 1),
        range(ord('A'), ord('Z') + 1),
        range(ord('a'), ord('z') + 1),
    ))

    def __init__(self):
        self.map_tiny_to_long_url: Dict[str, str] = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        tiny_url = None
        while tiny_url is None or tiny_url in self.map_tiny_to_long_url:
            tiny_url = ''.join(chr(chr_ord) for chr_ord in choices(self.VALID_CHR_ORDS, k=5))

        self.map_tiny_to_long_url[tiny_url] = longUrl
        return tiny_url

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        return self.map_tiny_to_long_url[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
