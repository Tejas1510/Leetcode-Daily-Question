# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
class Solution:
    def kWeakestRows(self, a: List[List[int]], k: int) -> List[int]:
        dict1 = defaultdict(int)
        for i in range(len(a)):
            dict1[i]=a[i].count(1)
        dict2=dict(sorted(dict1.items(),key=operator.itemgetter(1)))
        c=[]
        for k1,v in dict2.items():
            c.append(k1)
        return c[:k]
                