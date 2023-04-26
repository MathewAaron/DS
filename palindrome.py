"""
Given a string s, return true if it is a palindrome, or false otherwise.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        new_str = ""
        
        for i in s:
            
            if i.isalnum():
                new_str += i.lower()
                
        return new_str == new_str[::-1]