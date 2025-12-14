from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i,a in enumerate(nums):
            # Mira los duplicados, y si es uno avanza, pero se fija en que si es un duplicado hacia atras
            # si pide el siguiente se saldra del array
            if i > 0 and a == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                candidate = nums[i] + nums[left] + nums[right]
                if candidate == 0:
                    res.append(tuple([nums[i], nums[left], nums[right]]))
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1    
                elif candidate > 0:
                    right -= 1
                else:
                    left += 1  
        return res
    
    
def test():
    sol = Solution()
    tests = [
        ([0,0,0], [0,0,0])
        ([0,1,1],[]),
        ([-1,0,1,2,-1,-4],[[-1,-1,2],[-1,0,1]]),
        # sin solución
        ([1, 2, 3, 4], []),
        ([-5, -4, -3, -2], []),

        # mezcla con varias soluciones
        ([-2, -1, -1, 0, 1, 2, 2], [[-2, 0, 2], [-1, -1, 2], [-1, 0, 1]]),
        
        # duplicados pesados (debe devolver sin duplicar)
        ([-2, 0, 0, 2, 2], [[-2, 0, 2]]),
        ([-1, -1, -1, 2, 2], [[-1, -1, 2]]),
        ([-4, -2, -2, -2, 0, 1, 2, 2, 2, 4], [[-4, 0, 4], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]]),
        ]
    for nums, expected in tests:
        res = sol.threeSum(nums)
        ok = normalize(res) == normalize(expected)
        if ok:
            print(f"✅ nums={nums} -> {normalize(res)}")
        else:
            print(f"❌ nums={nums}")
            print(f"   expected={normalize(expected)}")
            print(f"   got     ={normalize(res)}")   

def normalize(triples):
    # Ordena cada tripleta y luego ordena el conjunto total para comparar sin depender del orden
    return sorted({tuple(sorted(t)) for t in triples})        
        
if __name__ == "__main__":
    test()