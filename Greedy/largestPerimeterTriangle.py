# https://leetcode.com/problems/largest-perimeter-triangle/
class Solution(object):
    def largestPerimeter(self, a):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=sorted(a,reverse=True)
        for i in range(1,len(a)-1):
            if(a[i-1]<a[i]+a[i+1]):
                return a[i-1]+a[i]+a[i+1]
        return 0
            