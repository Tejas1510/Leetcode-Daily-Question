# https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/
class Solution(object):
    def minSubsequence(self, a):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a.sort()
        ma=0
        ans=[]
        while(True):
            if(ma>sum(a)):
                return ans
            else:
                ans.append(a[-1])
                ma=ma+a[-1]
                a.pop()
        
            