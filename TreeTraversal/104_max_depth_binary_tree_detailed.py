"""
LeetCode 104: Maximum Depth of Binary Tree
------------------------------------------
Problem:
    Given the root of a binary tree, return its maximum depth.
    A binary tree's maximum depth is the number of nodes along
    the longest path from the root node down to the farthest leaf node.

Example:
        3
       / \
      9  20
         / \
        15  7

Output: 3

-------------------------------------------------------------
# Concepts:
    - Depth = number of levels (root level counted as 1)
    - Tree traversal can be done using:
        1. Recursive DFS (Depth-First Search)
        2. Iterative BFS (Breadth-First Search, Level-Order)
-------------------------------------------------------------
"""

from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# =====================================================================
# 1️⃣ RECURSIVE DFS APPROACH
# =====================================================================
"""
Approach:
    - If tree is empty → depth = 0
    - Otherwise, depth = 1 + max(depth of left subtree, depth of right subtree)

Reasoning:
    Each recursive call computes the depth for one subtree.
    The function unwinds bottom-up, combining results.

Time Complexity: O(N)  (each node visited once)
Space Complexity: O(H) (recursion stack, H = tree height)

Interview Note:
    ✅ Preferred first in interviews because it is clean and intuitive.
    🚫 May hit recursion depth limit in extremely deep trees.
"""

class SolutionRecursive:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return 1 + max(left_depth, right_depth)



# =====================================================================
# 2️⃣ ITERATIVE BFS APPROACH (LEVEL-ORDER TRAVERSAL)
# =====================================================================
"""
Approach:
    - Use a queue (collections.deque) to traverse tree level by level.
    - Each iteration of the outer while-loop represents one level.
    - Increment `depth` once per level.

Why BFS here:
    - Avoids recursion stack overflow for very deep trees.
    - Natural fit for problems requiring level-wise processing.

Time Complexity: O(N)
Space Complexity: O(W), where W = maximum width of the tree
"""

class SolutionIterative:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # -----------------------------------------------------------------
        # 💡 Doubt #1: Why not `queue = root.val`?
        #     Because root.val is just an integer, not a node.
        #     We need to traverse node objects to access their children.
        # -----------------------------------------------------------------

        # Initialize queue with root node (not its value)
        queue = deque([root])
        depth = 0

        while queue:
            # Each iteration = one full tree level
            depth += 1
            level_size = len(queue)

            # Process all nodes in this level before incrementing depth again
            for _ in range(level_size):
                # -------------------------------------------------------------
                # 💡 Doubt #2: What does `popleft()` do?
                #     Removes and returns the front node from queue (FIFO).
                #     Example: deque([3, 9, 20]) → popleft() → 3, remaining [9, 20]
                # -------------------------------------------------------------
                node = queue.popleft()

                # -------------------------------------------------------------
                # 💡 Doubt #3: Why append children to queue?
                #     Because they represent the next level in BFS order.
                # -------------------------------------------------------------
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return depth



# =====================================================================
# 📘 DOUBTS & EXPLANATIONS SUMMARY
# =====================================================================
"""
1️⃣ Why not `queue = root.val`?
-------------------------------------------------
    - `root` is a TreeNode object containing:
          root.val      → the integer value stored in that node
          root.left     → pointer to left child (TreeNode)
          root.right    → pointer to right child (TreeNode)

      When we do `queue = root.val`, we are storing only the integer,
      not the node. We then lose access to its children.

      BFS must visit nodes level by level and enqueue their children.
      Therefore, we must enqueue **the entire node object**, not its value.

    ✅ Correct:
        queue = deque([root])
    🚫 Incorrect:
        queue = root.val  # loses node structure

-------------------------------------------------

2️⃣ What does `queue = deque([root])` mean?
-------------------------------------------------
    - `deque` (double-ended queue) is imported from `collections`.
      It allows O(1) operations for both ends: `append()` and `popleft()`.

    - By doing `deque([root])`, we create a queue initialized with
      the root node as the first element.

    Visual representation:
        Front → [ root ] → Back

      Here, `root` is a TreeNode object, not its value.
      The queue will store multiple nodes as BFS progresses.

    Example:
        queue = deque([root])
        After processing:
            queue.append(root.left)
            queue.append(root.right)
        Now queue = [root.left, root.right]

-------------------------------------------------

3️⃣ What happens when we do `queue.popleft()`?
-------------------------------------------------
    - It removes and returns the **front-most element** of the queue
      (the oldest element added).

    - This ensures **FIFO** behavior (First-In, First-Out).

    Example:
        queue = deque([3, 9, 20])
        node = queue.popleft()  # node = 3
        queue becomes deque([9, 20])

    - We process this node (e.g., print it, or enqueue its children)
      and then move on to the next in queue.

-------------------------------------------------

4️⃣ What does `deque([3, 9, 20])` do?
-------------------------------------------------
    - Initializes a queue with three elements in order.
      The leftmost element (3) will be processed first.

    - Conceptually:
        Front [3, 9, 20] Back
        → popleft() returns 3
        → remaining queue = [9, 20]

    - In BFS, these elements represent nodes at the same level
      that will be processed sequentially.

-------------------------------------------------

5️⃣ Why use `for _ in range(len(queue))` inside the while loop?
-------------------------------------------------
    - At each iteration of the outer `while`, the queue contains
      all nodes of the current level.

    - We record its length as `level_size`, then process exactly
      that many nodes. Any children appended during this loop belong
      to the **next level** and will be processed in the next iteration.

    Example:
        Level 1: queue = [3]        → process one node
        Level 2: queue = [9, 20]    → process two nodes
        Level 3: queue = [15, 7]    → process two nodes

    This mechanism guarantees depth increments exactly once per level.

-------------------------------------------------

6️⃣ What does `depth += 1` represent?
-------------------------------------------------
    - Each time we finish processing all nodes in the current level,
      we have gone one level deeper into the tree.
      Therefore, incrementing `depth` tracks how many levels exist.

    Example:
        After processing level 1 → depth = 1
        After processing level 2 → depth = 2
        After processing level 3 → depth = 3

-------------------------------------------------

7️⃣ Which approach should be presented first in interviews?
-------------------------------------------------
    ✅ Step 1: Start with the **recursive DFS** solution.
        - Demonstrates understanding of recursion and divide-and-conquer.
        - Cleaner, easier to reason about.
    
    ✅ Step 2: Then mention the **iterative BFS** version.
        - Handles very deep trees safely.
        - Shows awareness of iterative traversal and memory considerations.

    Example interview statement:
        "I would first implement this recursively using DFS for clarity.
         Alternatively, we can use an iterative BFS approach with a queue
         to handle very deep trees without stack overflow."

-------------------------------------------------

8️⃣ When is BFS more robust than DFS?
-------------------------------------------------
    - When the tree is extremely deep (e.g., a skewed tree with 10^5 nodes),
      recursion might cause stack overflow.

    - BFS avoids recursion entirely by managing its own queue structure.

    - BFS is also preferred for:
        * Computing averages per level
        * Finding maximum width
        * Zigzag or level-order printing
        * Any problem where **level information** matters

-------------------------------------------------
"""


# =====================================================================
# 🧩 SHORT DRY RUN EXAMPLE
# =====================================================================
"""
Tree:
       3
      / \
     9  20
        / \
       15  7

BFS Execution Trace:
------------------------------------------------
Initial queue: [3]
Depth = 0

→ Level 1: process [3]
   Enqueue children [9, 20]
   Depth = 1

→ Level 2: process [9, 20]
   Enqueue children [15, 7]
   Depth = 2

→ Level 3: process [15, 7]
   No new children
   Depth = 3

Queue empty → return depth = 3
------------------------------------------------
"""


# =====================================================================
# ✅ Optional Test Harness
# =====================================================================
if __name__ == "__main__":
    # Build sample tree
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    # Test both implementations
    print("Recursive DFS Depth :", SolutionRecursive().maxDepth(root))
    print("Iterative BFS Depth :", SolutionIterative().maxDepth(root))
