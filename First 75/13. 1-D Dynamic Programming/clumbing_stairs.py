    
    # You are given an integer n representing the number of steps to reach the top of a staircase. 
    # You can climb with either 1 or 2 steps at a time.
    # Return the number of distinct ways to climb to the top of the staircase.
    
class Solution:
    # recursive 
    def climbStairsRec(self, n: int) -> int:
        def dfs(i):
            #  if (i >= n) return i == n ? 1 : 0;
            if i >= n:
                return i == n 
            return dfs(i + 1) + dfs(i + 2)

        return dfs(0)
            
    def climbStairsCache(self, n: int) -> int:
        cache = [-1] * n
        def dfs(i):
            if i >= n:
                return i == n
            if cache[i] != -1:
                return cache[i]
            cache[i] = dfs(i + 1) + dfs(i + 2)
            return cache[i]

        return dfs(0)
    

    
    
    
    def climbStairsDBUp(self, n: int) -> int:
        i = 2
        dp = [1,2]
        
        while i <= n:
            temp = dp[1]
            dp[1] = dp[0] + dp[1]
            dp[0] = temp
            i += 1
        return dp[0]
    
    
    
    
    
    
    
def runTest():
    sol = Solution()
    testCases = [(0, 0), (1,1), (2,2), (3,3), (4, 5),(5,8),(6, 13), (10, 89)]
    
    for param, expected in testCases:
        res = sol.climbStairsDBUp(param)
        if res == expected:
            print(f"✅ numero de escalones -> {param}, maneras -> {expected}, solución -> {res}")
        else:
            print(f"✅ numero de escalones -> {param}, maneras -> {expected}, solución -> {res}")    



if __name__ == "__main__":
    runTest()