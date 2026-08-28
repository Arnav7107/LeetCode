class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # start = len(nums) - k
        # i = 0
        # while(start < len(nums)):
        #     nums[i], nums[start] = nums[start], nums[i]
        #     i += 1
        #     start += 1
        # print(nums)

        k = k % len(nums)

        nums[:] = nums[-k:] + nums[:-k]