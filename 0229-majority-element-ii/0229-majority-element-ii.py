class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = {}
        n = len(nums)
        ans = []
        target = n//3

        for i in range(n):
            if(nums[i] not in d):
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1
        
        for k,v in d.items():
            if(v > target):
                ans.append(k)
        return ans