# https://leetcode.com/problems/reduce-array-size-to-the-half/
from collections import Counter
class Solution:
    def minSetSize(self, a: List[int]) -> int:
        a1=dict(Counter(a))
        a1=dict(sorted(a1.items(),key=operator.itemgetter(1),reverse=True))
        b=a1.values()
        print(b)
        ans=0
        temp=0
        i=0
        for v in b:
            temp=temp+v
            ans=ans+1
            if(temp>=len(a)//2):
                return ans