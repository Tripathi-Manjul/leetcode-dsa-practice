#Brute Force -- O(n^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [] 
        
#How to create a hash-map for python list
#1- nums1idx = {n:i for i, n in enumerate(nums1)}
#2- for i in range(n):
            # numMap[nums[i]] = i

#Two-pass Hash Table -- O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        # Build the hash table ; 1st pass
        for i in range(n):
            numMap[nums[i]] = i

        # Find the complement ; 2nd pass
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i: #To make sure same element is not selected twice
                return [i, numMap[complement]]

        return []  # No solution found

    
#One-pass Hash Table -- O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        #Single pass
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i

        return []  # No solution found

                
        
