
"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        
        nums_set = {}

        for i in nums:

            if i in nums_set:

                return True

            else:
                nums_set[i] = 1

        return False
        