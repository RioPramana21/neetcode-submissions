class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_look = {}
        for i, num in enumerate(nums):
            if num in num_to_look:
                return [num_to_look[num], i]
            num_to_look[target-num] = i