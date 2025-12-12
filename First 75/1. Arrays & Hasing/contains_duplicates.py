from typing import List


class Solution:
    def hasDuplicateBruteForce(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

    def hasDuplicateSorted(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False

    def hasDuplicateHashSet(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if(num in seen): 
                return True
            seen.add(num)
        return False    



