class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indexes = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if num_indexes.get(difference) is not None:
                return [num_indexes.get(difference), i]
            else:
                num_indexes[nums[i]] = i