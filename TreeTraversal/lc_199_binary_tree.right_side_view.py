"""
LeetCode 199. Binary Tree Right Side View
------------------------------------------
Problem Statement:
------------------
Given the root of a binary tree, imagine yourself standing on its right side.
Return the values of the nodes you can see ordered from top to bottom.

Intuition:
----------
From the right side, you see the *rightmost node* of each depth level.
Perform a level-order (BFS) traversal:
    • Traverse each level from left to right.
    • Record the last node encountered at every level
      because it represents the visible node from the right.

Approach:
---------
1. Use a queue (collections.deque) for BFS traversal.
2. For each level:
      - Process all nodes in that level.
      - Enqueue children (left first, then right).
      - When processing the last node of the level
        (i == level_size - 1), append its value to result.
3. Continue until queue is empty.

Complexity:
-----------
Time Complexity:  O(N)   — Every node is visited once.
Space Complexity: O(W)   — W = maximum width of the tree (queue size).

Core Logic:
-----------
When processing the last node of each level (i == level_size - 1),
record its value in the result list.
"""

from collections import deque
from typing import Optional, List


class TreeNode:
    """Definition of a binary tree node."""
    def __init__(self, val: int,
                 left: Optional["TreeNode"] = None,
                 right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Perform BFS traversal to capture the rightmost node of each level.

        Args:
            root (TreeNode): Root of the binary tree.

        Returns:
            List[int]: Values of nodes visible from the right side.
        """
        if not root:
            return []

        result = []                # Stores visible node values
        queue = deque([root])      # Queue for level-order traversal

        # Process nodes level by level
        while queue:
            level_size = len(queue)  # Number of nodes in this level

            # Traverse one full level
            for i in range(level_size):
                node = queue.popleft()  # FIFO: ensures left-to-right order

                # Enqueue children for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                # Capture the rightmost node (last in this level)
                if i == level_size - 1:
                    result.append(node.val)

        return result


# --------------------------------------------------------------------
# DRY RUN EXAMPLE
# --------------------------------------------------------------------
# Example Tree:
#         1
#        / \
#       2   3
#        \   \
#         5   4
#
# Expected Output: [1, 3, 4]
#
# Explanation (Level-wise traversal):
# -----------------------------------
# Level | Nodes in Queue (L→R) | Rightmost Node | Result
# ------|-----------------------|----------------|--------
# 0     | [1]                   | 1              | [1]
# 1     | [2, 3]                | 3              | [1, 3]
# 2     | [5, 4]                | 4              | [1, 3, 4]

if __name__ == "__main__":
    # Constructing the example tree manually
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)

    sol = Solution()
    output = sol.rightSideView(root)

    print("Right Side View of the Binary Tree:", output)

    """
    Step-by-Step Queue Simulation:
    ------------------------------
    Initial Queue: [1]
    Process 1 → enqueue(2), enqueue(3) → append(1)

    Queue: [2, 3]
    Process 2 → enqueue(5)
    Process 3 → enqueue(4) → append(3)

    Queue: [5, 4]
    Process 5
    Process 4 → append(4)

    Final Output: [1, 3, 4]
    """
