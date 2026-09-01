class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = float('-inf')
        add = 0

        for i in range(len(nums)):
            add += nums[i]
            maxi = max(add, maxi)
            if(add < 0):
                add = 0
        return maxi