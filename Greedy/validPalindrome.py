# https://leetcode.com/problems/valid-palindrome-ii/
class Solution:
    def validPalindrome(self, s: str) -> bool:
        i,j=0,len(s)-1
        while(i<=j):
            if(i==j or i==j-1):
                return True
            if(s[i]==s[j]):
                i=i+1
                j=j-1
            else:
                t1=s[:i]+s[i+1:]
                if(t1==t1[::-1]):
                    return True
                t2=s[:j]+s[j+1:]
                if(t2==t2[::-1]):
                    return True
                return False
            