class Solution:
    def isValid(self, s: str) -> bool:
        open_par = {')': '(', '}': '{', ']':'['}
        stack = []
        for c in s:
            if c in open_par.values():
                stack.append(c)
            else:
                if (open_par[c] not in stack) or stack.pop() != open_par[c]:
                    return False
        return True if not(stack) else False