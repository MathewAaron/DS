// Given an array nums of integers, return how many of them contain an even number of digits.

class Solution {
public:
    int findNumbers(vector<int>& nums) {
        int count = 0,digits; 
        for(auto num: nums){   
            digits = 0;
            while(num){  
                num = num / 10; 
                digits = digits + 1;  
            }
            if(digits % 2 == 0){  
                count = count + 1; 
            }
        }
        return count; 
    }
};