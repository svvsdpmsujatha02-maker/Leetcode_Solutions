class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        index = 0
        for i in range(len(nums)):
            index = i
            first = nums[0:index]
            last = nums[index+1:]
            if sum(first) == sum(last):
                return i
                break
        else :
            return -1
        