class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int k = 0;
        for(int i = 0; i < nums.size() - k; i++){
            if(nums[i] == val){
                swap(nums[i--], nums[nums.size() - k - 1]);
                k++;
            }
        }
        return nums.size() - k;
    }

    void swap(int& a, int& b){
        int x = a;
        a = b;
        b = x;
    }
};