"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        digits = digits[::-1]
        
        carry_var = 1
        i = 0
        
        while carry_var:
            
            if i < len(digits):
                
                if digits[i] == 9:
                    digits[i] = 0 
                else:
                    digits[i] += 1
                    carry_var = 0
            else:
                digits.append(1)
                carry_var = 0
            i += 1
        digits = digits[::-1]

        return digits
            