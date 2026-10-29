# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # An empty subtree is always a subtree of any tree
        if not subRoot: 
            return True
        # If the main tree is empty but subRoot isn't, subRoot can't be a subtree
        if not root: 
            return False
        
        # Check if the trees match starting from the current node
        if self.sameTree(root, subRoot):
            return True
        
        # Recursively search the left and right children of the main tree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        # Both are empty -> identical
        if not s and not t:
            return True
        # One is empty or values don't match -> not identical
        if not s or not t or s.val != t.val:
            return False
        
        # Both values match, recursively check children
        return self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)
