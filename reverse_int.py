"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
"""
class Solution:
    def reverse(self, x: int) -> int:
        
        rev = 0
        
        MIN = -2147483648
        MAX = 2147483647
        while (int(x)):
            
            pop = int(math.fmod(x,10))
            
            x = int(x/10)
            
            if (rev > MAX //10 or (rev == MAX //10 and pop >= MAX % 10)): return 0
            elif (rev < MIN // 10 or (rev == MIN // 10 and pop <= MIN % 10)): return 0
            else:
                rev = (rev * 10) + pop
            
        return rev