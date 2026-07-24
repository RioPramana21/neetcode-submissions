class Solution:
    def isAnagram(self, s:str, t:str) -> bool:
        s_occurences = [0]*26 # all lowercase English alphabet
        for ch in s:
            s_occurences[ord(ch)-ord('a')] += 1
        
        t_occurences = [0]*26 # all lowercase English alphabet
        for ch in t:
            t_occurences[ord(ch)-ord('a')] += 1
        
        return s_occurences == t_occurences