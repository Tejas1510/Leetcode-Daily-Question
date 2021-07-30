# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
class Solution:
    def countNegatives(self, a: List[List[int]]) -> int:
        c=0
        for i in range(len(a)):
            for j in range(len(a[i])):
                if(a[i][j]<0):
                    c=c+1
        return c