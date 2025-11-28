class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0,0,0]
        for num in nums:
            counts[num] += 1
        i = 0
        for color, count in enumerate(counts):
            for _ in range(count):
                nums[i] = color
                i += 1   
    
tests = [
    # básicos
    ([0], [0]),
    ([1], [1]),
    ([2], [2]),
    ([0,1,2], [0,1,2]),
    ([2,1,0], [0,1,2]),

    # repetidos
    ([1,1,1], [1,1,1]),
    ([2,2,2], [2,2,2]),
    ([0,0,0], [0,0,0]),

    # ya ordenado
    ([0,0,1,1,2,2], [0,0,1,1,2,2]),

    # totalmente invertido
    ([2,2,1,1,0,0], [0,0,1,1,2,2]),

    # alternancia dura
    ([0,2,0,2,0,2], [0,0,0,2,2,2]),

    # patrón que rompe punteros
    ([2,1,0,1,2,0,1], [0,0,1,1,1,2,2]),

    # dominan los 1s
    ([1,1,1,0,2,1,1], [0,1,1,1,1,1,2]),

    # bloques grandes
    ([2,2,2,0,0,1,1,1,2,0,1], [0,0,0,1,1,1,1,2,2,2,2]),

    # solo 0s y 2s
    ([2,0,2,0,2,0], [0,0,0,2,2,2]),

    # solo 1s y 2s
    ([1,2,1,2,2,1], [1,1,1,2,2,2]),

    # solo 0s y 1s
    ([0,1,1,0,1,0], [0,0,0,1,1,1]),

    # stress test moderado
    ([2,0,1,2,1,0,1,2,0,1,2,0], sorted([2,0,1,2,1,0,1,2,0,1,2,0])),

    # zeros al final
    ([1,2,1,2,0,0,0], [0,0,0,1,1,2,2]),

    # zeros al principio
    ([0,0,0,1,2,1,2,1], [0,0,0,1,1,1,2,2]),

    # random
    ([1,0,2,2,1,0,0,1,2,1,0], sorted([1,0,2,2,1,0,0,1,2,1,0])),
]

# ------------------------------------------------------------
# Ejecutor
# ------------------------------------------------------------
solution = Solution()

for inp, expected in tests:
    nums = inp.copy()   # hacemos copia para no mutar la lista original del test
    
    try:
        solution.sortColors(nums)  # LeetCode style: no devuelve nada
    except Exception as e:
        print(f"❌ ERROR ejecutando nums={inp!r}: {e}")
        continue

    if nums == expected:
        print(f"✅ OK  nums={inp!r} → {nums}")
    else:
        print(f"❌ FAIL nums={inp!r} → {nums} (expected {expected})")
