#include <iostream>
#include <vector>
#include <string>
#include <cmath>

const std::string DESCRIPTION = "Given an integer array nums of size n, \
    return the number with the value closest to 0 in nums. \
    If there are multiple answers, return the number with the largest value.";

class Solution {
public:
    int findClosestNumber(std::vector<int>&);
};


int Solution::findClosestNumber(std::vector<int>& nums){
    int clos_val = abs(nums[0]);
    int clos_index = 0;
    for (size_t i{0}; i!=nums.size();++i){
        int abs_val = abs(nums[i]);
        if (clos_val >= abs_val){
            if (nums[clos_index] > nums[i] && clos_val == abs_val)
                continue;
            clos_val = abs_val;
            clos_index = i;
        }
    }
    return nums[clos_index];
}