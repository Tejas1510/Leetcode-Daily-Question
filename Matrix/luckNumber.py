# https://leetcode.com/problems/lucky-numbers-in-a-matrix/
class Solution:
    def luckyNumbers (self, a: List[List[int]]) -> List[int]:
        row = [min(row) for row in a]
        col = [max(col) for col in zip(*a)]
        return set(row) & set(col)

