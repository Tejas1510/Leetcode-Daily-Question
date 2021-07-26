# https://leetcode.com/problems/max-increase-to-keep-city-skyline/
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        max_rows=[max(row) for row in grid]
        max_cols=[max(col) for col in zip(*grid)]
        ans=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                ans=ans+min(max_rows[i],max_cols[j])-grid[i][j]
        return ans