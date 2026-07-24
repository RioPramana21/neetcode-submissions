class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for word in strs:
            word_occ = [0]*26
            for ch in word:
                word_occ[ord(ch)-ord('a')] += 1
            word_occ = tuple(word_occ)
            if word_occ in ans:
                ans[word_occ].append(word)
            else:
                ans[word_occ] = [word]
        return list(ans.values())