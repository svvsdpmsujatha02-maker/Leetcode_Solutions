class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0 :
            return 0
        a = 0
        b = 1
        c = 1
        for i in range(3,n+1) :
            d = a + b + c
            a = b 
            b = c
            c = d
        return c
        