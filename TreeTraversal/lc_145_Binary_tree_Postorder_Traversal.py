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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Perform a postorder traversal (Left -> Right -> Root) of the binary tree.

        ========================================================================
        POSTORDER TRAVERSAL CONCEPT
        ========================================================================
        Steps:
            1. Visit all nodes in the left subtree.
            2. Visit all nodes in the right subtree.
            3. Process (visit) the current node.

        Characteristics:
            - Visits children before their parent.
            - Useful for deleting trees, freeing resources,
              or evaluating postfix (Reverse Polish) expressions.

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

        1) postorderTraversal(1)
           -> dfs(1)
           -> dfs(1.left) -> dfs(None) returns
           -> dfs(1.right) -> dfs(2)

        2) dfs(2)
           -> dfs(2.left) -> dfs(3)
               dfs(3.left) -> None -> return
               dfs(3.right) -> None -> return
               visit(3) -> result = [3]
           -> dfs(2.right) -> None -> return
           -> visit(2) -> result = [3, 2]

        3) dfs(1)
           -> after right subtree, visit(1) -> result = [3, 2, 1]

        Final result: [3, 2, 1]

        ========================================================================
        COMPLEXITY
        ========================================================================
        - Time Complexity: O(N)   (Each node visited once)
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

            # STEP 1: Traverse left subtree
            dfs(node.left)

            # STEP 2: Traverse right subtree
            dfs(node.right)

            # STEP 3: Visit root (after both children)
            result.append(node.val)

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
    output = sol.postorderTraversal(root)
    # Expected postorder result: [3, 2, 1]
    assert output == [3, 2, 1], f"Expected [3, 2, 1], got {output}"

    # Edge cases
    assert sol.postorderTraversal(None) == []          # Empty tree
    assert sol.postorderTraversal(TreeNode(5)) == [5]  # Single node tree
