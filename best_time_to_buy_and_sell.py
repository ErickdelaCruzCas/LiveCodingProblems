class Solution:
    def bestTime(self, prices):
        min, diff = prices[0], 0
        for num in prices:
            if num < min: min = num
            aux_diff = num - min
            if aux_diff > diff: diff = aux_diff
        return diff;    


tests = [
    ([10,1,5,6,7,1], 6),
    ([10,8,7,5,2], 0),
    ([1,2], 1)
]


for (param, res) in tests:
    try:
        my_res = Solution().bestTime(param)
        if my_res == res:
            print("✅")
        else:
            print(f"❌ Result: {my_res}, expected: {res}")  
    except Exception as e:
        print(f"❌ -> {e}")
            
  
        

