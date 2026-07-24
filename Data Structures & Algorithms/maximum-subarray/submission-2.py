class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_value = max_value = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            curr_value = max(curr_value, 0)
            curr_value += num
            max_value = max(max_value, curr_value)

        return max_value