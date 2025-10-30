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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Perform an inorder traversal (Left -> Root -> Right) of the binary tree.

        ========================================================================
        INORDER TRAVERSAL CONCEPT
        ========================================================================
        Steps:
            1. Visit all nodes in the left subtree.
            2. Process (visit) the current node.
            3. Visit all nodes in the right subtree.

        This traversal order ensures that:
        - For a Binary Search Tree (BST), values are visited in sorted order.
        - Each node is processed after its left subtree but before its right.

        ========================================================================
        WALKTHROUGH EXAMPLE: root = [1, null, 2, 3]
        ========================================================================
        Tree structure:
                1
                 \
                  2
                 /
                3

        Step-by-step trace:

        1) inorderTraversal(1)
           -> dfs(1)
           -> dfs(1.left) -> dfs(None) returns
           -> visit(1) -> result = [1]
           -> dfs(1.right) -> dfs(2)

        2) dfs(2)
           -> dfs(2.left) -> dfs(3)
               dfs(3.left) -> None -> return
               visit(3) -> result = [1, 3]
               dfs(3.right) -> None -> return
           -> visit(2) -> result = [1, 3, 2]
           -> dfs(2.right) -> None -> return

        3) dfs(1) returns
           Final result = [1, 3, 2]

        ========================================================================
        COMPLEXITY
        ========================================================================
        - Time Complexity: O(N)  (Each node visited once)
        - Space Complexity:
            * Recursion stack: O(H), where H = tree height
            * Result list: O(N)
        ========================================================================
        """

        result: List[int] = []

        def dfs(node: Optional[TreeNode]) -> None:
            # BASE CASE
            if node is None:
                return

            # STEP 1: Traverse the left subtree
            dfs(node.left)

            # STEP 2: Visit the root node
            result.append(node.val)

            # STEP 3: Traverse the right subtree
            dfs(node.right)

        dfs(root)
        return result


# ============================================================================
# EXAMPLE USAGE AND VALIDATION
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
    output = sol.inorderTraversal(root)
    # Expected inorder result: [1, 3, 2]
    assert output == [1, 3, 2], f"Expected [1, 3, 2], got {output}"

    # Edge cases
    assert sol.inorderTraversal(None) == []          # Empty tree
    assert sol.inorderTraversal(TreeNode(5)) == [5]  # Single node tree
