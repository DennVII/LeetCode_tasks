class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        reversed = str(x)[::-1]
        return str(x) == reversed
        

