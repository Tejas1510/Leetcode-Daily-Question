# https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/
class Solution(object):
    def minOperations(self, a):
        ans=0
        for i in range(1,len(a)):
            if(a[i]>a[i-1]):
                pass
            else:
                ans=ans+abs(a[i]-a[i-1])+1
                a[i]=a[i-1]+1
        return ans
        