# https://leetcode.com/explore/featured/card/july-leetcoding-challenge-2021/611/week-4-july-22nd-july-28th/3824/
 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if(not root):
            return None
        root.left=self.pruneTree(root.left)
        root.right=self.pruneTree(root.right)
        
        if(root.val==0 and not root.right and not root.left):
            return None
        else:
            return root
        