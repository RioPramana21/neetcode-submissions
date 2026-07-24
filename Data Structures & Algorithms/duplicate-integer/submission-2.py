class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        occurences = {}
        for num in nums:
            occurences[num] = occurences.get(num, 0) + 1
            if occurences[num] == 2:
                return True
        return False