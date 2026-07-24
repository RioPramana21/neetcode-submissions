class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        occurences = {}
        for num in nums:
            if occurences.get(num):
                return True
            occurences[num] = 1 
        return False