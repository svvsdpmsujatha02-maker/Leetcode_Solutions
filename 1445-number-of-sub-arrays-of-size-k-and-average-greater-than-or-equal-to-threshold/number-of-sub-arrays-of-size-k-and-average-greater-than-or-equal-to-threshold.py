class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        '''
        count = 0
        for i in range(0,len(arr)-k+1):
            sums = 0
            for j in range(i,i+k):
                sums += arr[j]
            if sums / k >= threshold :
                count += 1
        return count
        '''
        l = 0
        r = k-1
        count = 0
        sums = 0
        for i in range(0,r+1):
            sums += arr[i]
        if sums / k >= threshold :
            count += 1
        while r < len(arr)-1:
            sums = sums - arr[l]
            l += 1
            r += 1
            sums = sums + arr[r]
            if sums / k >= threshold :
                count += 1
        return count


        