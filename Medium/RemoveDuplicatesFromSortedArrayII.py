class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pointer = 0
        counter = 0
        for i in range(1, len(nums)):
            if counter < 1 and nums[pointer] == nums[i] or nums[pointer] != nums[i]:
                if nums[pointer] == nums[i] and counter < 1:
                    counter += 1
                elif nums[pointer] != nums[i]:
                    counter = 0
                pointer += 1
                nums[pointer] = nums[i]
        if counter:
            nums[pointer] = nums[len(nums) - 1]
        return pointer + 1

