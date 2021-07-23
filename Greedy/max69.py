# https://leetcode.com/problems/maximum-69-number/
class Solution(object):
    def maximum69Number (self, num):
            num=str(num)
            a=list(num)
            for i in range(len(a)):
                if(a[i]=="6"):
                    a[i]="9"
                    break
            return ("".join(a))
        