class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        list1 = []
        list2 = []
        list3 = []
        for i in range(len(nums)):
            if nums[i] < pivot :
                list1.append(nums[i])
            elif nums[i] == pivot :
                list2.append(nums[i])
            else :
                list3.append(nums[i])
        ans = list1 + list2 + list3
        return ans
        