# https://leetcode.com/problems/partition-labels/
from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dict1=defaultdict(int)
        for i in range(len(s)):
            dict1[s[i]]=i
        l=0
        r=0
        a=[]
        for i in range(len(s)):
            r=max(r,dict1[s[i]])
            if(r==i):
                a.append(r-l+1)
                l=i+1
        return a