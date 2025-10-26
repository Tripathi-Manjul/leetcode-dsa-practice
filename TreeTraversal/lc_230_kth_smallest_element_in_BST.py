"""
Approach:
----------
We use an *iterative inorder traversal* with an explicit stack.
In a BST, inorder traversal (Left → Node → Right) visits nodes in sorted order.
Therefore, the kth node visited during this traversal is the kth smallest element.

Complexity:
------------
Time Complexity:  O(H + k), where H is the height of the tree.
Space Complexity: O(H), due to the stack storing up to H nodes.
H can be O(log N) for balanced trees and O(N) for skewed trees.
"""

from typing import Optional

class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val: int,
                 left: Optional["TreeNode"] = None,
                 right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Iterative inorder traversal to find the kth smallest element in a BST.

        Args:
            root (TreeNode): Root node of the BST.
            k (int): The index (1-based) of the smallest element to find.

        Returns:
            int: The value of the kth smallest node.

        Raises:
            ValueError: If k is invalid (larger than the number of nodes).
        """

        # Stack to simulate recursive inorder traversal
        stack = []
        node = root

        # Continue traversal until kth element is found
        while True:

            # 1. Go as left as possible, pushing nodes onto stack
            while node is not None:
                stack.append(node)
                node = node.left

            # 2. Pop from stack -> next node in inorder sequence
            if not stack:
                # Defensive check — k is larger than node count
                raise ValueError("Invalid input: k exceeds number of nodes in BST")

            node = stack.pop()
            k -= 1  # Decrement k each time we visit a node

            # 3. When k reaches zero, current node is kth smallest
            if k == 0:
                return node.val

            # 4. Otherwise, move to the right subtree and continue
            node = node.right


# -----------------------------------------------------------
# DRY RUN EXAMPLE
# -----------------------------------------------------------
# Example Tree:
#         5
#        / \
#       3   7
#      / \   \
#     2   4   9
#
# k = 4  → Expected output: 5
#
# Inorder Traversal Order → [2, 3, 4, 5, 7, 9]
# The 4th smallest element is 5.

if __name__ == "__main__":
    # Constructing the example BST manually
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(9)

    sol = Solution()
    k = 4
    result = sol.kthSmallest(root, k)

    print(f"The {k}th smallest element in the BST is: {result}")

    """
    Step-by-step Dry Run:
    ----------------------
    Stack  |  Node  |  Action                        | k | Output
    -------------------------------------------------------------
    []      |  5     | push(5), move left             | 4 |
    [5]     |  3     | push(3), move left             | 4 |
    [5,3]   |  2     | push(2), move left (None)      | 4 |
    [5,3,2] | None   | pop(2), visit -> k=3           | 3 |
    [5,3]   | None   | pop(3), visit -> k=2           | 2 |
    [5]     |  4     | push(4), move left(None)       | 2 |
    [5,4]   | None   | pop(4), visit -> k=1           | 1 |
    [5]     | None   | pop(5), visit -> k=0 -> return 5
    -------------------------------------------------------------
    Result: 5
    """
