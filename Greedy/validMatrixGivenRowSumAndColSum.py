# https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n=len(rowSum)
        m=len(colSum)
        mat=[[0 for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                temp=min(rowSum[i],colSum[j])
                mat[i][j]=temp
                rowSum[i]-=temp
                colSum[j]-=temp
        return mat