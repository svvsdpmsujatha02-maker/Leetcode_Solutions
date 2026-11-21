class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = []
        s = 0
        for i in range(n):
            s += nums[i]
            ans.append(s)
        return ans
            

        