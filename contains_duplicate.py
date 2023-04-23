
"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""
from collections import defaultdict
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        
        nums_set = defaultdict(int)

        for i in nums:

            nums_set[i] += 1

        for i in nums_set:

            if nums_set[i] == 1:
                return i 
        