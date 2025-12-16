from typing import List


class Solution:
    
     # Prefix Suffix
    def maxSubarraySumCircular1(self, nums: List[int]) -> int:
        n = len(nums)
        right_max = [0] * n
        right_max[-1] = nums[-1]
        suffix_sum = nums[-1]

        for i in range(n - 2, -1, -1):
            suffix_sum += nums[i]
            right_max[i] = max(right_max[i + 1], suffix_sum)

        max_sum = nums[0]
        cur_max = 0
        prefix_sum = 0

        for i in range(n):
            cur_max = max(cur_max, 0) + nums[i]
            max_sum = max(max_sum, cur_max)
            prefix_sum += nums[i]
            if i + 1 < n:
                max_sum = max(max_sum, prefix_sum + right_max[i + 1])

        return max_sum
    
    # Kadane
    def maxSubarraySumCircular2(self, nums: List[int]) -> int:
        globMax, globMin = nums[0], nums[0]
        currMax, currMin = 0,0
        total = 0
        for n in nums:
            currMax = max(currMax + n, n)
            currMin = min(currMin + n, n)
            total += n
            globMax = max(globMax, currMax)
            globMin = min(globMin, currMin)

        return max(globMax, total - globMin) if globMax > 0 else globMax