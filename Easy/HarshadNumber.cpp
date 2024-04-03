#include <iostream>
#include <string>

const std::string DESCRIPTION = "\
An integer divisible by the sum of its digits is said to be a Harshad number. \
You are given an integer x. Return the sum of the digits of x if x is a Harshad number, otherwise, return -1.";


class Solution {
public:
    int sumOfTheDigitsOfHarshadNumber(int x) {
        int summa = 0;
        int xc = x;
        while(xc){
            summa += xc % 10;
            xc /= 10;
        }
        return (x % summa) ? -1 : summa;
    }
};
