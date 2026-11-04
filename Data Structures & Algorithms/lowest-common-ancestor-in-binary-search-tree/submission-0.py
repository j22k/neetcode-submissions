# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # LCA must be grater or equal to p and q
        # node == p or q then node is LCA

        self.p = p
        self.q = q

        if not root:
            return None
        
        def dfs(r):
            if not r:
                return None

            if r.val == self.p.val or r.val == self.q.val:
                return r
            if self.p.val < r.val and self.q.val < r.val:
                return dfs(r.left)
            if self.p.val > r.val and self.q.val > r.val:
                return dfs(r.right)
            return r
            
        return dfs(root)