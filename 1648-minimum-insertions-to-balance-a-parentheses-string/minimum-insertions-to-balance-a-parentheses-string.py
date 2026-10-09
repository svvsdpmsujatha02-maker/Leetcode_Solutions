class Solution:
    def minInsertions(self, s: str) -> int:
        insertion = 0
        open = 0
        i = 0
        while i < len(s) :
            if s[i] == '(' :
                open += 1
            else :
                if open > 0 :
                    if i + 1 < len(s) and s[i+1] == ')' :
                        open -= 1
                        i += 1
                    else :
                        insertion += 1
                        open -= 1
                else :
                    insertion += 1
                    if i + 1 < len(s) and s[i+1] == ')' :
                        i += 1
                    else :
                        insertion += 1
            i += 1
        insertion += open * 2
        return insertion
        