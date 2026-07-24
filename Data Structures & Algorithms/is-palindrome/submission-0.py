class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(" ", "")
        s = "".join(char for char in s if char.isalnum())
        return (s == s[::-1])