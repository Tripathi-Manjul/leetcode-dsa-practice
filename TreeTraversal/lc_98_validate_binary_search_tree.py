# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    """
    Binary Tree Node definition.
    Each node stores an integer value and has optional left/right children.
    """
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Validate whether a given binary tree is a Binary Search Tree (BST).

    A valid BST satisfies:
        - All nodes in the left subtree have values strictly less than the current node's value.
        - All nodes in the right subtree have values strictly greater than the current node's value.
        - Both left and right subtrees must themselves be valid BSTs.

    Core Idea:
        Perform a Depth-First Search (DFS) while maintaining a valid numeric range (lower, upper)
        for each node. Each node must satisfy lower < node.val < upper.

        - Left subtree → upper bound becomes node.val
        - Right subtree → lower bound becomes node.val

    This enforces the global BST property across all levels.
    """

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Entry point for BST validation.

        Args:
            root (TreeNode): Root of the binary tree.
        Returns:
            bool: True if valid BST, False otherwise.
        """

        def helper(node: Optional[TreeNode], lower: float, upper: float) -> bool:
            """
            Recursive helper that validates a subtree within (lower, upper) bounds.

            Args:
                node (TreeNode): Current node under validation.
                lower (float): Minimum allowed value (exclusive).
                upper (float): Maximum allowed value (exclusive).
            Returns:
                bool: True if subtree rooted at 'node' is a valid BST.
            """
            # Base case: An empty subtree is always valid.
            if not node:
                return True

            val = node.val

            # Current node must lie strictly within valid bounds.
            if val <= lower or val >= upper:
                return False

            # Validate right subtree:
            # Values must be greater than current node's value and less than upper bound.
            if not helper(node.right, val, upper):
                return False

            # Validate left subtree:
            # Values must be less than current node's value and greater than lower bound.
            if not helper(node.left, lower, val):
                return False

            # If both subtrees are valid, return True.
            return True

        # Start recursion with infinite bounds.
        return helper(root, float('-inf'), float('inf'))


"""
==========================
🧭 DRY RUN EXAMPLE
==========================

Tree:
        5
       / \
      3   7
     / \   \
    2   4   8

Step 1:
helper(node=5, lower=-inf, upper=inf)
    ✅  -inf < 5 < inf
    → Check right: helper(7, 5, inf)
    → Check left:  helper(3, -inf, 5)

Step 2 (Right Subtree):
helper(node=7, lower=5, upper=inf)
    ✅  5 < 7 < inf
    → Check right: helper(8, 7, inf)
    → Check left:  helper(None, 5, 7)

    helper(8, 7, inf) → ✅ 7 < 8 < inf
        → right=None ✅
        → left=None ✅
    ✅ Subtree rooted at 7 is valid

Step 3 (Left Subtree):
helper(node=3, lower=-inf, upper=5)
    ✅  -inf < 3 < 5
    → Check right: helper(4, 3, 5)
    → Check left:  helper(2, -inf, 3)

    helper(4, 3, 5) → ✅ 3 < 4 < 5
        → right=None ✅
        → left=None ✅
    helper(2, -inf, 3) → ✅ -inf < 2 < 3
        → right=None ✅
        → left=None ✅
    ✅ Subtree rooted at 3 is valid

Step 4:
All recursive calls returned True → ✅ Entire tree is a valid BST.

==========================
❌ Invalid Example
==========================
If the left subtree has a node '6' under '3':

        5
       / \
      3   7
     / \
    2   6   ← violates BST property (6 > 5)

Dry Run:
helper(node=6, lower=3, upper=5)
    ❌ 6 not < 5 → returns False

Final Output: False
==========================
"""
