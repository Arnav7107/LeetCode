class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0: 1}
        curr_sum = 0
        count = 0

        for i in range(len(nums)):
            curr_sum += nums[i]
            
            if(curr_sum - k in d):
                count += d[curr_sum - k]
            if(curr_sum not in d):
                d[curr_sum] = 1
            else:
                d[curr_sum] += 1
            
        return count
            










        # add = 0
        # start = 0
        # count = 0

        # for i in range(len(nums)):
        #     add += nums[i]
        #     if(add == k):
        #         count += 1
        #     if(add > k):
        #         while(add > k and start <= i):
        #             add -= nums[start]
        #             if(add == k):
        #                 count += 1
        #             start += 1
        # return count
