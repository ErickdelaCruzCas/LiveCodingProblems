from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ini, fin = 0, len(heights) - 1
        maxArea = 0
        while ini < fin:
            base = fin - ini
            print(f"ini: {ini}, fin: {fin}, base:{base}")
            area = min(heights[ini], heights[fin]) * base
            print(f"area: {area}")
            maxArea = max(area, maxArea)
            if heights[ini] < heights[fin]:
                ini += 1
            else:
                fin -= 1    
        return maxArea