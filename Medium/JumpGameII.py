DESCRIPTION = '''
You are given a 0-indexed array of integers nums of length n. 
You are initially positioned at nums[0].
Each element nums[i] represents the maximum length of a forward jump from index i. 
In other words, if you are at nums[i], you can jump to any nums[i + j] where:
    0 <= j <= nums[i] and
    i + j < n
Return the minimum number of jumps to reach nums[n - 1]. 
The test cases are generated such that you can reach nums[n - 1].
'''

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        journey = [float("inf")] * n
        journey[0] = 0
        for i in range(n - 1):
            for j in range(nums[i] + 1):
                if (i + j) >= n:
                    break
                journey[i + j] = min(journey[i + j], journey[i] + 1)
        return journey[n-1]
