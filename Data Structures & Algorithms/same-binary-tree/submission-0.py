# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(P,Q):
            if not P and not Q:
                return True
            if not P or not Q:
                return False
            if P.val != Q.val:
                return False
            return dfs(P.left, Q.left) and dfs(P.right,Q.right)
            
        return dfs(p, q)