"""
Copy List with Random Pointer — Approaches Summary
==================================================

Problem:
---------
Given a linked list where each node has:
- next pointer to the next node
- random pointer to any node (or null)

Goal: Construct a **deep copy** of the list, where:
- Each new node is a separate object
- next and random pointers correctly mirror the original list
- No pointer in the copied list should reference the original nodes

---

Notation:
---------
- X = original node
- x = copy of X

---

APPROACH 1: HashMap / Two-Pass Method
-------------------------------------
Idea: Maintain a mapping from each original node to its copy.

Steps:
1. First pass: Create copy nodes and store mapping
    - Iterate original list:
        map[X] = x   # x = Node(X.val)
    - At this stage, copy nodes exist but next/random not assigned

2. Second pass: Assign next and random pointers
    - For each original node X:
        x = map[X]
        x.next = map.get(X.next, None)
        x.random = map.get(X.random, None)

3. Return map[head] as the new head of the copied list

Complexity:
- Time: O(n)
- Space: O(n) for the HashMap

---

APPROACH 2: Interleaving Trick (O(n) time, O(1) space)
-------------------------------------------------------
Idea: Interleave copy nodes in the original list to avoid extra space.

Steps:

1. Interleave copies with original nodes
----------------------------------------
For every original node X, create its copy x and insert it right after X:

    Before: X → Y → Z
    After:  X → x → Y → y → Z → z

- X.next points to its copy x
- Copy nodes (x) are temporarily mixed in the original list

2. Assign random pointers for copied nodes
------------------------------------------
For every original node X:
    x.random = X.random.next   # if X.random is not null

Explanation:
- X.next = copy of X → x
- X.random = original node Y
- Y.next = copy of Y → y
- Therefore, x.random points to the correct copy of the target node

Example:
Original: A.random → C
Copy:     a.random → c

3. Separate the original and copied lists
-----------------------------------------
Restore the original list and extract the copied list:

    X.next = X.next.next   # link original nodes together
    x.next = x.next.next   # link copy nodes together

Result:
- Original list is restored to its original structure
- Copied list is fully independent, with correct next and random pointers

---

Key Observations:
-----------------
1. Each original node points immediately to its copy (X.next = x)
2. Random assignment leverages adjacency: x.random = X.random.next
3. After separation, both lists are independent and correctly wired

---

Complexity Comparison:
----------------------
Approach 1 (HashMap):
- Time: O(n)
- Space: O(n)

Approach 2 (Interleaving Trick):
- Time: O(n)
- Space: O(1) extra
"""


#Approach 1: Iterative HashMap (Two-Pass)
# Definition for a Node.
class Node:
    def __init__(self, val: int, next: 'Node' = None, random: 'Node' = None):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        # Step 1: Create copy nodes and store mapping from original -> copy
        old_to_new = {}  # Dictionary: original node -> copied node
        current = head
        while current:
            old_to_new[current] = Node(current.val)
            current = current.next

        # Step 2: Assign next and random pointers using the map
        current = head
        while current:
            copy_node = old_to_new[current]
            copy_node.next = old_to_new.get(current.next)      # None if current.next is None
            copy_node.random = old_to_new.get(current.random)  # None if current.random is None
            current = current.next

        # Step 3: Return head of the copied list
        return old_to_new[head]

#Approach 2: Interleaving Trick (O(1) extra space)
# Definition for a Node.
class Node:
    def __init__(self, val: int, next: 'Node' = None, random: 'Node' = None):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        # Step 1: Interleave copy nodes with original nodes
        current = head
        while current:
            copy_node = Node(current.val)
            copy_node.next = current.next
            current.next = copy_node
            current = copy_node.next

        # Step 2: Assign random pointers for copies
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next  # Move to next original node

        # Step 3: Separate original and copied lists
        original = head
        copy_head = head.next
        copy = copy_head
        while original:
            original.next = original.next.next
            if copy.next:
                copy.next = copy.next.next
            original = original.next
            copy = copy.next

        return copy_head
