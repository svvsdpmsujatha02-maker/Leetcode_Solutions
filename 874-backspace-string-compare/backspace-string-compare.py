class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_1 = []
        stack_2 = []
        for ch in s :
            if ch != '#' :
                stack_1.append(ch)
            elif stack_1 :
                stack_1.pop()
        for ch in t :
            if ch != '#' :
                stack_2.append(ch)
            elif stack_2 :
                stack_2.pop()
        return stack_1 == stack_2