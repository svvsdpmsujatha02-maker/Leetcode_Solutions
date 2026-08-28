class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a1 = int(a,2)
        b1 = int(b,2)
        c = a1 + b1 
        d = bin(c)
        return d[2:]
        