# https://leetcode.com/problems/richest-customer-wealth/
class Solution:
    def maximumWealth(self, a: List[List[int]]) -> int:
        row = [sum(i) for i in a]
        return max(row)