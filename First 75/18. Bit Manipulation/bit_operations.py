

# AND
n = 1 & 1

# OR
n = 1 | 0

# XOR
n = 0 ^ 1

# NOT (negation)
n = ~n

# Bit shifting
n = 1
n = n << 1
n = n >> 1

# Counting Bits
def countBits(n):
    count = 0
    while n > 0:
        if n & 1:
            count += 1
        n = n >> 1 # same as n // 2
    return count


def hammingWeightBuiltIn(self, n: int) -> int:
    return bin(n).count('1')


# Count bits in an array of integers
def countBits(self, n: int) -> List[int]:
    res = []
    for num in range(n + 1):
        one = 0
        for i in range(32):
            if num & (1 << i):
                one += 1
        res.append(one)
    return res  

def reverseBits(n):
    res = 0
    for _ in range(32):
        res = (res << 1) | (n & 1)
        n >>= 1
    return res

def reverseBitsinBlock(self, n: int) -> int:
    res = n
    res = (res >> 16) | (res << 16) & 0xFFFFFFFF
    res = ((res & 0xff00ff00) >> 8) | ((res & 0x00ff00ff) << 8)
    res = ((res & 0xf0f0f0f0) >> 4) | ((res & 0x0f0f0f0f) << 4)
    res = ((res & 0xcccccccc) >> 2) | ((res & 0x33333333) << 2)
    res = ((res & 0xaaaaaaaa) >> 1) | ((res & 0x55555555) << 1)
    return res & 0xFFFFFFFF