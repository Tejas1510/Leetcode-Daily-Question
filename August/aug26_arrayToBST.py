# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/611/week-4-july-22nd-july-28th/3827/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, a: List[int]) -> TreeNode:
        if not a:
            return None
        mid=len(a)//2
        root = TreeNode(val=a[mid])
        root.left=self.sortedArrayToBST(a[:mid])
        root.right=self.sortedArrayToBST(a[mid+1:])
        return root