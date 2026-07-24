class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        occurences = defaultdict(int)
        for num in nums:
            if num in occurences: return True
            occurences[num] += 1
        return False