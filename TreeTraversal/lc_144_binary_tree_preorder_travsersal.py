from __future__ import annotations
from typing import Optional, List

class TreeNode:
    """
    Standard binary tree node definition.
    """
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Return the preorder traversal (Root -> Left -> Right) of the binary tree.

        Implementation: recursive DFS helper that appends node values to 'result'.

        ========================================================================
        TRAVERSAL TYPES REFERENCE (for later review)
        ========================================================================

        1) **Preorder Traversal (Root → Left → Right)**
           - Visit the current node first.
           - Traverse the left subtree.
           - Traverse the right subtree.
           Example sequence for:
                 1
                  \
                   2
                  /
                 3
             Output: [1, 2, 3]

        2) **Inorder Traversal (Left → Root → Right)**
           - Traverse the left subtree.
           - Visit the current node.
           - Traverse the right subtree.
           Example sequence for same tree:
                 1
                  \
                   2
                  /
                 3
             Output: [1, 3, 2]

        3) **Postorder Traversal (Left → Right → Root)**
           - Traverse the left subtree.
           - Traverse the right subtree.
           - Visit the current node.
           Example sequence for same tree:
                 1
                  \
                   2
                  /
                 3
             Output: [3, 2, 1]

        ========================================================================
        WALKTHROUGH: Preorder traversal for root = [1, null, 2, 3]
        ========================================================================
        Tree structure:
                1
                 \
                  2
                 /
                3

        Call trace and 'result' evolution:

        preorderTraversal(root=1)
          result = []
          -> dfs(1)
             append(1)  → result = [1]
             dfs(1.left) → dfs(None) → returns
             dfs(1.right) → dfs(2)
                append(2) → result = [1, 2]
                dfs(2.left) → dfs(3)
                    append(3) → result = [1, 2, 3]
                    dfs(3.left) → None → return
                    dfs(3.right) → None → return
                dfs(2.right) → None → return
          return result = [1, 2, 3]

        ========================================================================
        COMPLEXITY ANALYSIS
        ========================================================================
        - Time Complexity: O(N), each node visited once.
        - Space Complexity:
            * Recursion stack: O(H), where H = tree height.
              Worst-case (skewed tree): O(N)
              Best-case (balanced tree): O(log N)
            * Result list: O(N)
        ========================================================================
        """

        result: List[int] = []

        def dfs(node: Optional[TreeNode]) -> None:
            # BASE CASE: if node is None, stop recursion.
            if node is None:
                return

            # VISIT ROOT (Preorder step 1)
            result.append(node.val)

            # TRAVERSE LEFT (Preorder step 2)
            dfs(node.left)

            # TRAVERSE RIGHT (Preorder step 3)
            dfs(node.right)

        # Start recursion from root.
        dfs(root)
        return result


# ============================================================================
# EXAMPLE USAGE AND QUICK TESTS
# ============================================================================
if __name__ == "__main__":
    # Construct example tree:
    #     1
    #      \
    #       2
    #      /
    #     3
    n3 = TreeNode(3)
    n2 = TreeNode(2, left=n3)
    root = TreeNode(1, right=n2)

    sol = Solution()

    output = sol.preorderTraversal(root)
    # Expected preorder: [1, 2, 3]
    assert output == [1, 2, 3], f"Expected [1, 2, 3], got {output}"

    # Validate on edge cases
    assert sol.preorderTraversal(None) == []          # Empty tree
    assert sol.preorderTraversal(TreeNode(5)) == [5]  # Single node tree

    # Quick reference outputs for same tree (manual reasoning):
    # Inorder: [1, 3, 2]
    # Postorder: [3, 2, 1]
