class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = ('(', '{', '[')
        closed_brackets = (')', '}', ']')
        queue = []
        for bracket in s:
            if bracket in open_brackets:
                queue.append(bracket)
            elif len(queue) == 0:
                return False
            elif (bracket == ')') and (queue.pop() == '('):
                continue
            elif (bracket == '}') and (queue.pop() == '{'):
                continue
            elif (bracket == ']') and (queue.pop() == '['):
                continue
            else:
                return False
        if len(queue) == 0:
            return True
        else: return False
                