DESCRIPTION = '''
You have n coins and you want to build a staircase with these coins. 
The staircase consists of k rows where the ith row has exactly i coins. 
The last row of the staircase may be incomplete.
Given the integer n, return the number of complete rows of the staircase you will build.
'''


class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        rows = 0
        step = 1
        while n - step >= 0:
            rows += 1
            n -= step
            step += 1
            
        return rows
