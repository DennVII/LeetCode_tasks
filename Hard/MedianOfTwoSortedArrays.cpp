#include<iostream>
#include<string>
#include<vector>
using namespace std;

const string DESCRIPTION = "Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays. \
The overall run time complexity should be O(log (m+n)).";

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        double median;
        vector<int> merged;
        auto iter1 = nums1.begin();
        auto iter2 = nums2.begin();
        while(iter1 != nums1.end() && iter2 !=nums2.end()){
            if(*iter1 < *iter2){
                merged.push_back(*iter1);
                ++iter1;
            }
            else{
                merged.push_back(*iter2);
                ++iter2;
            }
        }
        if(iter1!=nums1.end()){
            merged.insert(merged.end(), iter1, nums1.end());
        }
        if(iter2!=nums2.end()){
            merged.insert(merged.end(), iter2, nums2.end());
        }
        if(merged.size() % 2){
            median = 1.0 * merged[merged.size() / 2];
        }
        else{
            median =  1.0 *(merged[merged.size() / 2] + merged[merged.size() / 2 - 1] )/ 2;
        }
        return median;
    }
};
