"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        two_diff = defaultdict(int)
        
        for idx,num in enumerate(nums):
            
            if (target - num) in two_diff:
                
                return [idx,two_diff[target - num]]
            two_diff[num] = idx