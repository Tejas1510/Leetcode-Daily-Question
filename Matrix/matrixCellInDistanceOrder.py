# https://leetcode.com/problems/matrix-cells-in-distance-order/
class Solution:
    def allCellsDistOrder(self, r: int, c: int, r1: int, c1: int) -> List[List[int]]:
        a=[]
        for i in range(r):
            for j in range(c):
                a.append([i,j])
        dict1=defaultdict(list)
        for i in range(len(a)):
            t1=abs(r1-a[i][0])+abs(c1-a[i][1])
            dict1[tuple(a[i])]=t1
        finalAns=[]
        dict2=dict(sorted(dict1.items(),key=operator.itemgetter(1)))
        for k,v in dict2.items():
            finalAns.append(k)
        return finalAns
        
                