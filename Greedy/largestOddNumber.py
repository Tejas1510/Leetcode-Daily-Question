# https://leetcode.com/problems/largest-odd-number-in-string/
class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        for i in range(len(num)-1,-1,-1):
            if(int(num[i])%2!=0):
                return "".join(num[:i+1])
        return ""