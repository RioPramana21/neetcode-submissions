class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for string in strs:
            count = [0] * 26 # counting occ. of a-z in the string
            for char in string:
                count[ord(char) - ord('a')] += 1
            groups[tuple(count)].append(string)
        return list(groups.values())