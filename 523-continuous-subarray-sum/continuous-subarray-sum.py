class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        '''
        l = 0
        r = 0
        sums = 0
        n = len(nums)
        while r <= n - 1 :
            sums += nums[r]
            if sums % k == 0 and r-l+1 >= 2 :
                return True
                break
            while sums < k :
                sums = sums - nums[l]
                l += 1
            r = r + 1
        return False
        '''
        remainder_map = {0:-1}
        prefix = 0
        for i,num in enumerate(nums):
            prefix += num
            remainder = prefix % k
            if remainder in remainder_map :
                index = i - remainder_map[remainder]
                if  index >= 2 :
                    return True
            else:
                remainder_map[remainder] = i
        return False





        