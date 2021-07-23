# https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/
class Solution(object):
    def minCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: int
        """
        t1=0
        t2=0
        for i in range(len(position)):
            if(position[i]%2==0):
                t1=t1+1
            else:
                t2=t2+1
        return min(t1,t2)