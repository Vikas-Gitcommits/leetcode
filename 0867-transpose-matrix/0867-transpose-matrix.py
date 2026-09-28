class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        a=[[0]*len(matrix) for i in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                a[j][i]=matrix[i][j]
        return a
        