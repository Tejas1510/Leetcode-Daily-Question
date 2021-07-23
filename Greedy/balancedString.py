# https://leetcode.com/problems/split-a-string-in-balanced-strings/
class Solution(object):
    def balancedStringSplit(self, s):
        a=[]
        for i in range(len(s)):
            if(s[i]=="R"):
                a.append(1)
            else:
                a.append(-1)
        for i in range(1,len(a)):
            a[i]=a[i]+a[i-1]
        return a.count(0)
        