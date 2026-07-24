class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        max_area = 0
        while l < r:
            left_height, right_height = heights[l], heights[r]
            curr_area = (r-l) * min(left_height, right_height)
            max_area = max(max_area, curr_area)
            if left_height < right_height:
                l += 1
            else:
                r -= 1
        return max_area