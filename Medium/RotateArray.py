class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        additional_array = nums[len(nums) - k:]
        nums[k:] = nums[:len(nums) - k]
        nums[:k] = additional_array

