from typing import List


class Solution:
     
    # Canonical Prefix
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        for i in range(n):
            left = prefix[i]
            right = prefix[n] - prefix[i + 1]
            if left == right:
                return i
        return -1

    # Optimized version
    # def pivotIndex(self, nums: List[int]) -> int:
    #     total = sum(nums)
    #     leftsSum = 0
    #     for i in range(len(nums)):
    #         total -= nums[i]
    #         if total == leftsSum:
    #             return i
    #         leftsSum += nums[i]
    #     return -1   