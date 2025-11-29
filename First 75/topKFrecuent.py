class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frec = {}
        for num in nums:
            frec[num] = 1 + frec.get(num, 0)
        ordenados = sorted(frec.items(), key=lambda kv: kv[1], reverse=True)
        return [num for num, freq in ordenados[:k]]

    def topKFrequentBucket(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res