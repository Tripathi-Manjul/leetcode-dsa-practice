from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Perform a level-order (BFS) traversal of a binary tree.
        Returns a list of lists, where each inner list contains node values at one level.

        Example:
            Input: [3, 9, 20, null, null, 15, 7]
            Output: [[3], [9, 20], [15, 7]]
        """
        if not root:
            return []

        result = []
        queue = deque([root])

        # Process level by level
        while queue:
            level_size = len(queue)
            level_nodes = []

            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_nodes)

        return result
