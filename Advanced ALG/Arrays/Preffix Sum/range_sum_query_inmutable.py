from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.preSum = nums
        for i in range(len(nums)-1):
            self.preSum[i+1] += self.preSum[i]

       
        

    def sumRange(self, left: int, right: int) -> int:
        if (left - 1) < 0 or (right + 1) > (len(self.preSum) - 1):
            return self.preSum[left - 1, right + 1]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)