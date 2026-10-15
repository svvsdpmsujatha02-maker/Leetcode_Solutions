class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(n):
            for j in range(i,n):
                subarray = nums[i:j+1]
                distinct = len(set(subarray))
                total += distinct ** 2
        return total
        