class Solution(object):
    def maximumUnits(self,boxTypes, truckSize):
        boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        ans=0
        for box in boxTypes:
            n=min(truckSize,box[0])
            truckSize-=n
            ans=ans+n*box[1]
            if(truckSize==0):
                break
        return ans