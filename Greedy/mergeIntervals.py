# https://leetcode.com/problems/merge-intervals/
class Solution:
    def merge(self, a: List[List[int]]) -> List[List[int]]:
        a=sorted(a,key=lambda x:x[0])
        l=a[0][0]
        r=a[0][1]
        b=[]
        
        for i in range(1,len(a)):
            if(a[i][0]<=r and a[i][1]>=l):
                r=max(r,a[i][1])
                l=min(l,a[i][0])
            else:
                b.append([l,r])
                l=a[i][0]
                r=a[i][1]
        b.append([l,r])
        return b
            