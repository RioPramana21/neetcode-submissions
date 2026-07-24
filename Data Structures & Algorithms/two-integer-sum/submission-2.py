class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_to_look = {}
        for index, num in enumerate(nums):
            if num in nums_to_look:
                return [nums_to_look[num], index]
            nums_to_look[target-num] = index