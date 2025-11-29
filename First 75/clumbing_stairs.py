    
    # You are given an integer n representing the number of steps to reach the top of a staircase. 
    # You can climb with either 1 or 2 steps at a time.
    # Return the number of distinct ways to climb to the top of the staircase.
    
class Solution1:
    # recursive 
    def climbStairs(self, n: int) -> int:
        def dfs(i):
            if i >= n:
                return i == n
            return dfs(i + 1) + dfs(i + 2)

        return dfs(0)
            
            
            
class Solution2:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n
        def dfs(i):
            if i >= n:
                return i == n
            if cache[i] != -1:
                return cache[i]
            cache[i] = dfs(i + 1) + dfs(i + 2)
            return cache[i]

        return dfs(0)