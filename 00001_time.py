# Time: O(n)
# Space: O(n)


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainders = {}
        for i in range(len(nums)):
            if nums[i] in remainders:
                return [remainders[nums[i]], i]
            remainders[target-nums[i]] = i
