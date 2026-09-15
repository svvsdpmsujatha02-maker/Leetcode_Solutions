class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxi = 0
        for customer in accounts :
            wealth = sum(customer)
            maxi = max(maxi,wealth)
        return maxi
        