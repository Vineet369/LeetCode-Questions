class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        index_X = []
        index_Y = []        
                
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    index_X.append(i)
                    index_Y.append(j)
        index_X = set(index_X)
        index_Y = set(index_Y)
        print(index_X, index_Y)
        for i in (index_X):
            for j in range(col):
                matrix[i][j] = 0
                print(matrix)
        for i in (index_Y):
            for j in range(row):
                matrix[j][i] = 0
                print(matrix)
                      




a = Solution()
b = a.setZeroes([[1,1,1],[1,0,1],[1,1,1]])
print(b)