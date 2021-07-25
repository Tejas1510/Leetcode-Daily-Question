# https://leetcode.com/problems/assign-cookies/
class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        i=0
        j=0
        ans=0
        while(i<len(g) and j<len(s)):
            if(g[i]<=s[j]):
                ans=ans+1
                i=i+1
                j=j+1
            else:
                j=j+1
        return ans
            