# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        for i in range(len(s)):
            if(s[i]=="("):
                stack.append("(")
            else:
                if("(" in stack):
                    stack.pop()
                else:
                    stack.append(")")
        return len(stack)