# https://leetcode.com/explore/featured/card/july-leetcoding-challenge-2021/611/week-4-july-22nd-july-28th/3828/
class Solution:
    def threeSumClosest(self, a: List[int], target: int) -> int:
        a.sort()
        closestSum=a[0]+a[1]+a[-1]
        
        for i in range(0,len(a)-2):
            start=i+1
            end=len(a)-1
            while(start<end):
                curSum = a[i]+a[start]+a[end]
                if(curSum>target):
                    end=end-1
                else:
                    start=start+1
                if(abs(closestSum-target)>abs(curSum-target)):
                    closestSum=curSum
        return closestSum
        
                    