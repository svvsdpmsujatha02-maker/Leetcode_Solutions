class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        difference = 0
        product = 1
        sums = 0
        while n != 0 :
            d = n % 10 
            product = product * d
            sums += d
            n = n // 10
        difference = product - sums
        return difference


        