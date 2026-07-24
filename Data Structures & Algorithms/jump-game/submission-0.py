class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal_index = len(nums) - 1
        for i in range(goal_index-1, -1, -1):
            if i + nums[i] >= goal_index:
                goal_index = i
        return goal_index == 0