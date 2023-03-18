#include <iostream>



class Solution {
public:
  int mySqrt(int x){
    int low = 1, high = x, mid;
    while(low <= high){
      mid = low + (high - low)
    }
  }
  
  
  int mySqrt(int x) {
    // TODO: Write your code here
    for (int num = 1; ; num++){
      if (num * num < x){
        continue;
      }
      else{
        if (num * num > x){
          return num - 1;
        }
        else{
          return num;          
          }
      }
    }
    return 0;
  }
};
