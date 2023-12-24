class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(':')', '{':'}', '[':']'}
        stack = []
        for i in s:
            if i in brackets:
                stack.append(i)
            else:
                if len(stack) == 0 or i != brackets[stack.pop()]:
                    return False
        return len(stack) == 0