class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        
        def findK(piles, k):
            hours = 0
            for i in range(len(piles)):
                hours += math.ceil(piles[i] / k)
            print(hours)
            return hours
        
        left = 1
        right = max(piles)

        while(left <= right):
            mid = left + (right - left) // 2

            hours = findK(piles, mid)
            if(hours <= h):
                right = mid - 1
            else:
                left = mid + 1
        return left



        
# 1 2 3 4 5 6 7 8 9 10 11