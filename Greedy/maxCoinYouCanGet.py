# https://leetcode.com/problems/maximum-number-of-coins-you-can-get/
class Solution:
    def maxCoins(self, a: List[int]) -> int:
        a=sorted(a,reverse=True)
        ans=0
        b=[]
        i=0
        j=i+1
        k=-1
        print(a)
        while(len(b)<len(a)//3):
            b.append([a[i],a[j],a[k]])
            i=i+2
            j=i+1
            k=k-1
        print(b)
        for i in b:
            i.sort()
            print(i)
            ans=ans+i[1]
        return ans