class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_occ, t_occ = defaultdict(int), defaultdict(int)
        for ch in s:
            s_occ[ch] += 1
        for ch in t:
            t_occ[ch] += 1
        return s_occ == t_occ