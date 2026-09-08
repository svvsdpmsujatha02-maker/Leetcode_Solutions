class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        size = max(nums) + 1
        hash_array = [0]*size
        count = 0
        for i in range(len(nums)):
            hash_array[nums[i]] += 1
        for i in range(len(hash_array)):
            if hash_array[i] < 2 :
                continue
            count = 0
            for j in range(1,hash_array[i]+1):
                if hash_array[i] % j == 0 :
                    count += 1
            if count == 2 :
                return True
        return False
        

        