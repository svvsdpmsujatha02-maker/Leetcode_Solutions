class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum < 1 or sum > num * 9 :
            return ""
        result = []
        remaining = sum
        for i in range(num):
            left = num - i - 1 
            low = max(0,remaining - left * 9 )
            high = min(9 , remaining)
            if low > high :
                return ""
            result.append(str(high))
            remaining -= high
        return "".join(result)

        