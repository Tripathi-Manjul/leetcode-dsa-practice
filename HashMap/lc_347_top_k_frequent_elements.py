from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """
        LeetCode 347: Top K Frequent Elements

        Approach: Bucket Sort (O(n))
        -----------------------------------
        1. Count frequency of each number using Counter.
        2. Create "buckets" where index = frequency, and each bucket stores
           the numbers that appear exactly that many times.
        3. Traverse buckets from highest frequency to lowest,
           collecting numbers until we have k results.
        """

        # Step 1: Count frequencies of each element
        freq = Counter(nums)   # Example: [1,1,1,2,2,3] -> {1:3, 2:2, 3:1}
        
        # Step 2: Create buckets.
        # We need len(nums) + 1 buckets because the maximum possible frequency
        # of any number is len(nums) (all elements are the same).
        buckets = [[] for _ in range(len(nums) + 1)]

        # Place each number into its corresponding frequency bucket
        for num, count in freq.items():
            buckets[count].append(num)
        
        # Step 3: Collect results from high frequency to low
        result = []
        # Iterate backwards: from most frequent (len(nums)) down to 1
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:   # stop once we have k elements
                    return result


# Example run
nums = [1]
k = 1
sol = Solution()
print(sol.topKFrequent(nums , k))   # Expected output: [1]
