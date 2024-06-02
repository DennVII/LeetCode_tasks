class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        duplicates = {}
        i = 0
        k = 0
        while i < len(nums) - k:
            if nums[i] not in duplicates:
                duplicates[nums[i]] = 0
            else:
                nums[i], nums[len(nums) - k - 1] = nums[len(nums) - k - 1], nums[i]
                i -= 1
                k += 1
            i += 1
        nums[0: len(nums) - k] = sorted(nums[0: len(nums) - k])
        return len(nums) - k


