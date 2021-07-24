# https://leetcode.com/problems/longest-palindrome/
from collections import Counter
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        a=Counter(s)
        ans=0
        flag=0
        for v in a.values():
            if(v%2==0):
                ans=ans+v
            else:
                flag=1
                ans=ans+(v-1)
        if(flag==1):
            return ans+1
        else:
            return ans
                