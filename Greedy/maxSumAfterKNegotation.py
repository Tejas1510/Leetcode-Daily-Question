# https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/
class Solution(object):
    def largestSumAfterKNegations(self, a, k):
        a.sort()
        for i in range(len(a)):
            if(a[i]<0 and k>0):
                a[i]=-1*a[i]
                k=k-1
        sum1=sum(a)
        if(k%2==0):
            return sum1
        else:
            min1=min(a)
            sum1=sum1-2*min1
            return sum1