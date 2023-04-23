"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
"""

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        
        count = 0
        insert_idx = 1 
        for i in range(1,len(nums)):
            
            if nums[i-1] != nums[i]:
                
                nums[insert_idx] = nums[i]
                insert_idx += 1

        return insert_idx