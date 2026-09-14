# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         left = 0 
#         right = len(nums) - 1  
#         start = -1
#         end = -1

#         while(left <= right):
#             mid = left + (right - left) // 2
            
#             if(nums[mid] == target):
#                 temp1 = mid 
#                 temp2 = mid 
#                 while temp1 > 0 and nums[temp1 - 1] == target:
#                     temp1 -= 1
#                 while temp2 < len(nums) - 1 and nums[temp2 + 1] == target:
#                     temp2 += 1
#                 return [temp1, temp2]
            
#             if(nums[mid] > target):
#                 right = mid - 1
#             else:
#                 left = mid + 1
#         return [start, end]
        

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binary_search(nums, target, is_searching_left):
            left = 0
            right = len(nums) - 1
            idx = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    idx = mid
                    if is_searching_left:
                        right = mid - 1
                    else:
                        left = mid + 1
            
            return idx
        
        left = binary_search(nums, target, True)
        right = binary_search(nums, target, False)
        
        return [left, right]
            