class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # act cat
        # a -> 1, c -> 1, t -> 1
        # tac
        # dictionary:
        # {(a -> 1, c -> 1, t -> 1) : ["act", "cat"]}
        ans = {}
        for word in strs:
            freq = [0] * 26
            # act
            # a -> 97 -> 0 (ascii(ch) - ascii('a'))
            # b -> 98 -> 1
            for ch in word:
                freq[ord(ch) - ord('a')] += 1
            
            freq = tuple(freq)
            if freq in ans:
                ans[freq].append(word)
            else:
                ans[freq] = [word]
        return list(ans.values())