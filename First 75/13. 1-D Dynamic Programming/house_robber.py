from typing import List


class Solution:
    
    def robRecursive(self, nums: List[int]) -> int:
        def dfs(i): 
            if i >= len(nums):
                return 0
            return max(dfs(i + 1), nums[i] + dfs(i + 2))
        return dfs(0)
    
    def robMemo(self, nums: List[int]) -> int:
        cache = {}
        def dfs(i):
            if i >= len(nums):
                return 0
            if i in cache:
                return cache[i]
            cache[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))
            return cache[i]
        return dfs(0)
    
    def robDynSpaceOpt(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for num in nums:
            temp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
    
    
    
def runTest():
    sol = Solution()
    testCases = [
        ([1,1,3,3], 4), 
        ([2,9,8,3,6], (16))
        ]
    
    for param, expected in testCases:
        res = sol.robDynSpaceOpt(param)
        if res == expected:
            print(f"✅ Casas -> {param}, calculado -> {expected}, solución -> {res}")
        else:
            print(f"❌ Casas -> {param}, calculado -> {expected}, solución -> {res}")    



if __name__ == "__main__":
    runTest()