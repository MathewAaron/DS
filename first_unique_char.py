"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
"""

from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        s = list(s)
        
        letters_table = defaultdict(int)
        
        # count all occurences of each letter
        for i in s:
            
            if i not in letters_table:
                letters_table[i] = 1
            else :
                letters_table[i] += 1
        # return index of first number
        for idx, key in enumerate(s):

            if letters_table[key] == 1:

                return idx
        return -1