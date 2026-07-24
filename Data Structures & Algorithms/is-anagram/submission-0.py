class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars, t_chars = {}, {}
        for char in s:
            if s_chars.get(char):
                s_chars[char] += 1
            else:
                s_chars[char] = 1
        for char in t:
            if t_chars.get(char):
                t_chars[char] += 1
            else:
                t_chars[char] = 1
        return (s_chars == t_chars)