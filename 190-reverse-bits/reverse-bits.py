class Solution:
    def reverseBits(self, n: int) -> int:
        a = bin(n)
        b = a[2:].zfill(32)
        c = b[::-1]
        return int(c,2)

        
        