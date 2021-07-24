# https://leetcode.com/problems/lemonade-change/
class Solution(object):
    def lemonadeChange(self, a):
        five,ten=0,0
        for i in a:
            if(i==5):
                five+=1
            elif(i==10):
                if not five:
                    return False
                five-=1
                ten+=1
            else:
                if(five and ten):
                    five-=1
                    ten-=1
                elif(five>=3):
                    five-=3
                else:
                    return False
        return True
                
        