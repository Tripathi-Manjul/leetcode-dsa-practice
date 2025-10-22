# =============================
# LeetCode 101. Symmetric Tree
# =============================
# Problem: Given a binary tree, determine if it is symmetric around its center.
# A tree is symmetric if the left subtree is a mirror reflection of the right subtree.
#
# Thought Process:
# ----------------
# 1. Symmetry is a "mirror property" — we need to compare two subtrees at a time.
# 2. For any two nodes t1 and t2 to be mirrors:
#    - Both must be None → True
#    - One is None and the other is not → False
#    - Values must be equal → recursively check t1.left with t2.right and t1.right with t2.left
# 3. Recursion naturally models this "mirrored comparison" down the tree.
# 4. A helper function is needed because we must compare two nodes/subtrees simultaneously.
# 5. The main function triggers the recursion by comparing root.left and root.right.
# ----------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root):
        """
        Determines whether the binary tree is symmetric.
        :param root: TreeNode
        :return: bool
        """
        # ----------------
        # Base case: empty tree is symmetric
        # ----------------
        if not root:
            return True

        # ----------------
        # Helper function: recursively check if two subtrees are mirrors
        # ----------------
        def isMirror(t1, t2):
            """
            Checks if two trees t1 and t2 are mirror images.
            :param t1: TreeNode
            :param t2: TreeNode
            :return: bool
            """
            # ----------------
            # Doubt #1: Why do we need this helper function?
            # Answer: The symmetry check requires comparing two nodes simultaneously.
            # Main function has only one parameter (root), recursion needs two nodes (t1, t2).
            # ----------------

            # ----------------
            # Base case: both nodes are None → symmetric
            # ----------------
            if not t1 and not t2:
                return True

            # ----------------
            # Base case: one node is None or values differ → asymmetric
            # Doubt #2: Why two return statements?
            # Answer: These represent two mutually exclusive base cases:
            #    1) Both nodes None → return True
            #    2) Structural mismatch or value mismatch → return False
            # ----------------
            if not t1 or not t2 or t1.val != t2.val:
                return False

            # ----------------
            # Recursive case: check mirrored children
            # Doubt #3: How recursion checks next level?
            # Answer: Each recursive call compares:
            #    - t1.left ↔ t2.right (outer)
            #    - t1.right ↔ t2.left (inner)
            # This naturally moves down the tree until all leaves are checked.
            # ----------------
            return isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)

        # ----------------
        # Start recursion: compare left and right subtrees of the root
        # Doubt #4: Why return isMirror(root.left, root.right)?
        # Answer: The main function must return the result from the helper.
        #         This triggers recursion with the first mirrored pair (root.left, root.right).
        # ----------------
        return isMirror(root.left, root.right)
