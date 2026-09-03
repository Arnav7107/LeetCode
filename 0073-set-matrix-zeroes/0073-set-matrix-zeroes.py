class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        zero_row = [False] * n
        zero_col = [False] * m 
        for i in range(n):
            for j in range(m):
                if(matrix[i][j]==0):
                    zero_row[i] = True
                    zero_col[j] = True
        
        for i in range(n):
            for j in range(m):
                if(zero_row[i] or zero_col[j]):
                    matrix[i][j]=0