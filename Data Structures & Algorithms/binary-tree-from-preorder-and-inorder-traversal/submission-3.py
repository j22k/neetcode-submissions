from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Build a hash map for O(1) index lookups in the inorder list
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        # Iterator to cleanly pick the root from preorder sequentially
        preorder_iter = iter(preorder)
        
        def helper(left: int, right: int) -> Optional[TreeNode]:
            # Base case: no elements left in the current subtree range
            if left > right:
                return None
            
            # Fetch the next root value sequentially from preorder
            root_val = next(preorder_iter)
            root = TreeNode(root_val)
            
            # Find where this root splits the inorder array
            mid = inorder_map[root_val]
            
            # Process left subtree first (matches Preorder sequence: Root -> Left -> Right)
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            
            return root
            
        return helper(0, len(inorder) - 1)
