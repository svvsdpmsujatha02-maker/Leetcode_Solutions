class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        distinct_nums = set(nums)
        if len(distinct_nums) < 3:
            return max(distinct_nums)
        for i in range(2):
            distinct_nums.remove(max(distinct_nums))
        return max(distinct_nums)