# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/
class Solution:
    def minPairSum(self, a: List[int]) -> int:
        a.sort()
        b=[]
        for i in range(len(a)//2):
            b.append(a[i]+a[-i-1])
        return max(b)