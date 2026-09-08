class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        ans.append([1])
        for j in range(1, numRows):
            temp = []
            for i in range(j + 1):
                if(i == 0 or i == j):
                    temp.append(1)
                else:
                    temp.append(ans[j-1][i-1] + ans[j-1][i])
            ans.append(temp)
        return ans

    


        