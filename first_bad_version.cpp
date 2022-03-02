#include<bits/stdc++.h>
using namespace std;

/*
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

*/

class Solution {
public:
    int firstBadVersion(int n) {
        int low = 1, high = n, mid = 0;
        
        while(low < high){
            
            mid = low + (high-low)/2;
            
            if (isBadVersion(mid) == true){
                high =  mid;
            }
            else {
                low = mid + 1;
            }
            }
        return low;
        }
};