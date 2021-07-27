# https://leetcode.com/problems/bulb-switcher-iv/
class Solution:
    def minFlips(self, s: str) -> int:
        state="0"
        ans=0
        for i in range(len(s)):
            if(s[i]==state):
                pass
            else:
                if(state=="0"):
                    state="1"
                else:
                    state="0"
                ans=ans+1
        return ans