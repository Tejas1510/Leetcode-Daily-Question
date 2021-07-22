class Solution(object):
    def partitionDisjoint(self, a):
        ma=a[0]
        mi=a[-1]
        a1=[]
        a1.append(ma)
        a2=[]
        a2.append(mi)
        for i in range(1,len(a)):
            if(ma>=a[i]):
                a1.append(ma)
            else:
                ma=a[i]
                a1.append(a[i])
        for i in range(len(a)-2,-1,-1):
            if(mi<=a[i]):
                a2.append(mi)
            else:
                mi=a[i]
                a2.append(a[i])
        a2=a2[::-1]
        for i in range(len(a1)):
            if(a1[i]<=a2[i+1]):
                return (i+1)
                break
            else:
                pass