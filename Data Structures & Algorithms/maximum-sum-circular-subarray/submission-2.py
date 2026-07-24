class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # use kadane or find the min subarray
        curr_max_sum, curr_min_sum, total = 0, 0, 0
        max_sum, min_sum = nums[0], nums[0]
        for num in nums:
            total += num
            # -5, 4, -5, 1
            # -5, -1, -6, -5
            # curr_max_sum = 1
            curr_max_sum = max(curr_max_sum+num, num)
            curr_min_sum = min(curr_min_sum+num, num)

            max_sum = max(max_sum, curr_max_sum)
            min_sum = min(min_sum, curr_min_sum)
        return max(max_sum, total-min_sum) if max_sum > 0 else max_sum