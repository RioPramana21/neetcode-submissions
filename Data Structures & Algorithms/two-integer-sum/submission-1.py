class Solution:
    def twoSum(self, nums:List[int], target:int) -> List[int]:
        # indices = {difference:index}

        # [3,4,5,6]
        # _3 + pair = 7
        # pair = 7-3 = 4
        # {4:0}

        # _4 in dict
        # [0, 1]

        indices = {}
        for i, num in enumerate(nums):
            if num in indices:
                return [indices[num], i]
            indices[target-num] = i