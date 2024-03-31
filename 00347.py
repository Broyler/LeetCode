# Time: O(n)
# Space: O(n)


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = 1 + count.get(i, 0)
        
        bucket = [[] for _ in range(len(nums) + 1)]
        for i, c in count.items():
            bucket[c].append(i)

        result = []
        for i in range(len(nums), 0, -1):
            for j in bucket[i]:
                result.append(j)
                if len(result) == k:
                    return result
