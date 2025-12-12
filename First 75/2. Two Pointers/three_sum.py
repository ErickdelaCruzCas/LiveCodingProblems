class Solution:
    def three_sum(nums):
          print(nums)  
    
    
def test():
    sol = Solution()
    tests = [
        ((1,2,4),(2)),
        ((1,2,4),(2)),
        ((1,2,4),(2)),
        ((1,2,4),(2)), 
        ]
    for nums, expected in tests:
        res = sol.three_sum(nums)
        if res == expected:
            print(f"✅ numero de escalones -> {param}, maneras -> {expected}, solución -> {res}")
        else:
            print(f"✅ numero de escalones -> {param}, maneras -> {expected}, solución -> {res}")    

        
        
if __name__ == "__main__":
    test()