"""
loop each element

i + j = target
fix i

looped_element + j = target
we want to find j:

j = target - looped_element

hashMap = {j: index}

So j is always searchable in constant time, and it always
contain the earliest index since we loop from the start

time: O(N) -> loop nums
space: O(N) -> unique num in nums
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for index, num in enumerate(nums):
            pair = target - num
            if pair in hashMap:
                return [hashMap[pair], index]
            if num not in hashMap:
                hashMap[num] = index
