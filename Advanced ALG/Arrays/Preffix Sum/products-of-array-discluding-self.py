class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * len(nums)
        preffix = [1] * len(nums)
        suffix = [1] * len(nums)
        
        for i in range(1,n):
            preffix[i] = preffix[i - 1] * nums[i - 1]
        for i in range(n-2,-1,-1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        for i in range(n):
            res[i] = preffix[i] * suffix[i]
        return res

    def productExceptSelfOpt(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i] 
        postfix = 1
        for i in range(len(nums) -1 , -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res