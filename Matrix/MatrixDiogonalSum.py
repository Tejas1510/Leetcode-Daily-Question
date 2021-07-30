# https://leetcode.com/problems/matrix-diagonal-sum/
class Solution:
    def diagonalSum(self, a: List[List[int]]) -> int:
        ans=0
        n=len(a)
        for i in range(len(a)):
                ans=ans+a[i][i]+a[i][-i-1]
                j=j+1
        return ans-a[n//2][n//2] if n%2==1 else ans