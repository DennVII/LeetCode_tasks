#include <iostream>
#include <list>
#include <string>
#include <limits>

const std::string DESCRIPTION = "Given a signed 32-bit integer x, return x with its digits reversed. \
If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0. \
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).";


class Solution {
private:
    bool negative = false;
public:
    int reverse(int x) {
        if (x < 0){
            negative = true;
        }
        int digit;
        int result = 0;
        while(x != 0){
            digit = x % 10;
            x /= 10;
            if (result < std::numeric_limits<int>::min() / 10 || result > std::numeric_limits<int>::max() / 10)
                return 0;
            result = result * 10 + digit;
        }
        if (negative && result > 0){
            result *= -1;
        }
        return result;
    }
};
