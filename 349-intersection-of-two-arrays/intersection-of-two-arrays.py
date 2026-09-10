class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1 = set(nums1)
        num2 = set(nums2)
        res = num1 & num2
        return list(res)
        """
        # by using sets i removed duplicates first
        num1 =set(nums1)
        num2 = set(nums2)
        # created a list to store the commom elements
        res = []
        #condition fo rchecking intersection
        for i in num1 :
            if i in num2 :
                res.append(i)
        return res

        Another approach
        
        num1 =set(nums1)
        num2 = set(nums2)
        res = num1.intersection(num2)
        return list(res)
        """

        

        