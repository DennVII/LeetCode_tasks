#include <iostream>
#include <string>
#include <vector>

const std::string DESCRIPTION = "Given a binary array nums, \
return the maximum number of consecutive 1's in the array.";

class Solution {
public:
    int findMaxConsecutiveOnes(std::vector<int>& nums) {
        int sequence = 0;
        int max_sequence = 0;
        for(size_t i{0}; i != nums.size(); ++i){
            if(nums[i] == 1)
                sequence++;
            else{
                max_sequence = max_sequence < sequence ? sequence : max_sequence;
                sequence = 0;
            }
        }
        max_sequence = max_sequence < sequence ? sequence : max_sequence;
        return max_sequence;
    }
};

