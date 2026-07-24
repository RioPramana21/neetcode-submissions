class Solution:
    def groupAnagrams(self, strs:List[str]) -> List[List[str]]:
        # anagram -> num of characters in the string (a-z)
        # stop, pots, tops -> s = 1, t = 1, o = 1, p = 1
        # opts, spot -> same set of characters
        # hashMap = {tuple([set of chars]) : [str]}
        # hashMap = {(s=1, t=1, o=1, p=1) : ['stop', 'pots']}
        # s=1, t=1, o=1, p=1 -> [0,0,0,0,....,0,1,0,...]
        hashMap = {}
        for string in strs:
            occurences = [0] * 26
            for char in string:
                occurences[ord(char)-ord('a')] += 1
            occurences = tuple(occurences)
            if occurences in hashMap:
                hashMap[occurences].append(string)
            else:
                hashMap[occurences] = [string]
        return list(hashMap.values())