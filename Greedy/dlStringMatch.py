# https://leetcode.com/problems/di-string-match/
class Solution(object):
    def diStringMatch(self, s):
        a=[]
        for i in range(len(s)+1):
            a.append(i)
        ans=[]
        for i in range(len(s)):
            if(s[i]=="I"):
                ans.append(a[0])
                a.remove(a[0])
            else:
                ans.append(a[-1])
                a.pop()
        return ans + a
        