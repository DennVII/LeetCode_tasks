DESCRIPTION = '''
Given n non-negative integers representing an
elevation map where the width of each bar is 1,
compute how much water it can trap after raining.
'''

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_index = 0
        max_val = height[0]
        for index in range(len(height)):
            if(height[index] > max_val):
                max_index = index
                max_val = height[max_index]
        trapped = 0
        l = 0
        local_max = height[l]
        while l < max_index:
            if local_max > height[l]:
                trapped += (local_max - height[l])
            else:
                local_max = height[l]
            l += 1
        r = len(height) - 1
        local_max = height[r]
        while r > max_index:
            if local_max > height[r]:
                trapped += (local_max - height[r])
            else:
                local_max = height[r]
            r -= 1

        return trapped
