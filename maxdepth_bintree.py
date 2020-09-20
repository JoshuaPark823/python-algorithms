"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
  /  |
  9  20
    /  |
   15   7
return its depth = 3.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        # Check if the root is present at all, if not, return 0
        if root is None:
            return 0

        # Recur both left and right subtrees
        else:
            depth_left = self.maxDepth(root.left)
            depth_right = self.maxDepth(root.right)

            # Apply a ternary operator to decide which is larger
            depth = depth_left + 1 if depth_left > depth_right else depth_right + 1

            return depth