"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
"""

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range (len(nums)-k,len(nums)):
            last_num = nums.pop()
            nums.insert(0,last_num)
            
        