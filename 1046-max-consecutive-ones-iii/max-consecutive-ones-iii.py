class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        zero_count = 0
        max_length = 0
        n = len(nums)
        while r < n :
            if nums[r] == 0 :
                zero_count += 1
            while zero_count > k :
                if nums[l] == 0 :
                    zero_count -= 1
                l += 1
            if zero_count <= k :
                max_length = max(max_length,r-l+1)
                r += 1
        return max_length
        