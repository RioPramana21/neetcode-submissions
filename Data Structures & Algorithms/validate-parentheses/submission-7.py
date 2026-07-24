class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = []
        for bracket in s:
            if bracket in ('(', '{', '['):
                open_brackets.append(bracket)
            elif not open_brackets:
                return False
            elif (bracket == ')') and (open_brackets.pop() != '('):
                return False
            elif (bracket == '}') and (open_brackets.pop() != '{'):
                return False
            elif (bracket == ']') and (open_brackets.pop() != '['):
                return False
        return not open_brackets