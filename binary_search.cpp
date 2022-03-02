#include<bits/stdc++.h>
using namespace std;


class Solution{

    public:
        int binary_search(int n){

            int low = 1, high = n, mid = 0;

            while(low < high){
                mid = low + (high - low)/2 ;

                if (binary_search(mid) == true){
                    high = mid;
                }
                else{
                    low = mid + 1;
                }
            }
            return low;
        }
};