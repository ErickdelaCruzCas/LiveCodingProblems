from typing import List


class Solution:
    def twoSumSort(self, nums: List[int], target: int) -> List[int]:
        a = []
        for i, num in enumerate(nums):
            a.append([num, i])
        a.sort()
        i = 0
        j = len(nums) - 1
        while i < j:
            candidate = a[i][0] + a[j][0]
            if candidate == target:
                return [min(a[i][1], a[j][1]),
                        max(a[i][1], a[j][1])]
            elif candidate < target:
                i += 1
            else:
                j -= 1
        return []
    
    
    
    def twoSumMapTwoPass(self, nums: List[int], target: int) -> List[int]:
        indexes = {}
        for i, num in enumerate(nums):
            indexes[num] = i
        for i, num in enumerate(nums):
            current = target - num
            if current in indexes and indexes[current] != i:
                return [i, indexes[current]]
        return []
    
    
    def twoSumMapOnePass(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in prev:
                return [prev[diff], i]
            prev[num] = i
        return []
    
    
    
def test():
    solution = Solution()
    tests = [
        ((3,4,5,6),(7), ([0, 1])),
        ((4,5,6),(10), ([0, 2])),
        ((5,5),(10), ([0, 1])),
        ((1,2,4),(5), ([0, 2])), 
        ]
    for nums, target, sol in tests:
        res = solution.twoSumMapOnePass(nums, target)
        if res == sol:
            print(f"✅ nums -> {nums}, target -> {target}, solución -> {sol}, res -> {res}")
        else:
            print(f"❌ nums -> {nums}, target -> {target}, solución -> {sol}, res -> {res}")    

        
        
if __name__ == "__main__":
    test()