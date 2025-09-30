# Filename: randomized_set.py

import random

class RandomizedSet:
    """
    RandomizedSet allows:
    1. insert(val) in O(1)
    2. remove(val) in O(1)
    3. getRandom() in O(1), returning each element with equal probability
    """

    def __init__(self):
        # Dynamic array (list) to store elements for O(1) random access
        self.arr = []
        # Dictionary (hashmap) mapping element value -> index in arr
        self.pos = {}

    def insert(self, val: int) -> bool:
        """
        Inserts val into the set if not already present.
        Returns True if inserted, False if already present.
        """
        if val in self.pos:
            return False
        # Append to array
        self.arr.append(val)
        # Store index of val in hashmap
        self.pos[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes val from the set if present.
        Returns True if removed, False if not found.
        """
        if val not in self.pos:
            return False

        # Index of element to remove
        idx = self.pos[val]
        # Last element in the array
        last_val = self.arr[-1]

        # Swap the element to remove with the last element
        self.arr[idx] = last_val
        # Update the hashmap for last element
        self.pos[last_val] = idx

        # Remove the last element (previously swapped)
        self.arr.pop()
        # Delete the element from hashmap
        del self.pos[val]

        return True

    def getRandom(self) -> int:
        """
        Returns a random element from the set.
        Each element has equal probability.
        """
        # random.choice picks a random index and returns element
        return random.choice(self.arr)


# --------------------------
# Optional: Simple Test
# --------------------------
if __name__ == "__main__":
    ops = ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
    vals = [[], [1], [2], [2], [], [1], [2], []]

    obj = None
    output = []

    for op, val in zip(ops, vals):
        if op == "RandomizedSet":
            obj = RandomizedSet()
            output.append(None)
        elif op == "insert":
            output.append(obj.insert(val[0]))
        elif op == "remove":
            output.append(obj.remove(val[0]))
        elif op == "getRandom":
            output.append(obj.getRandom())

    print(output)
    # Expected Output: [None, True, False, True, 2, True, False, 2] (random may vary)
