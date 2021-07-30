# https://leetcode.com/problems/flipping-an-image/
class Solution:
    def flipAndInvertImage(self, a: List[List[int]]) -> List[List[int]]:
        for i in range(len(a)):
            a[i]=a[i][::-1]
            for j in range(len(a)):
                if(a[i][j]==1):
                    a[i][j]=0
                else:
                    a[i][j]=1
        return a
                    