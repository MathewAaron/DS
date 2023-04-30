"""
Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.
"""

from collections import defaultdict
class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        
        word_map = defaultdict(list)
        for idx, word in enumerate(wordsDict):

            word_map[word].append(idx)

        print(word_map)

        return min([abs(x - y) for x in word_map[word1] for y in word_map[word2]])