# https://leetcode.com/problems/array-partition-i/
class Solution(object):
    def arrayPairSum(self, a):
        a.sort()
        ans=0
        for i in range(0,len(a),2):
            ans=ans+a[i]
        return ans