# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/611/week-4-july-22nd-july-28th/3826/
class Solution:
    def findIntegers(self, num):
        s = bin(num + 1)[2:]
        n = len(s)
        dp = [1, 2] + [0]*(n-2)
        print(dp)
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        print(dp)
        flag, ans = 0, 0
        for i in range(n):
            if s[i] == "0": continue
            if flag == 1: break
            if i > 0 and s[i-1] == "1": flag = 1
            ans += dp[-i-1]
        
        return ans
    