from typing import List

def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    """
    Return True if there are two distinct indices i and j in the array such that
    nums[i] == nums[j] and abs(i - j) <= k.
    """
    last_seen = {}  # maps number to its last seen index
    for i, num in enumerate(nums):
        if num in last_seen and i - last_seen[num] <= k:
            return True
        last_seen[num] = i
    return False
