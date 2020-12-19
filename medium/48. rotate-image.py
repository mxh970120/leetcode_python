'''
Author: mxh970120
Date: 2020.12.19
'''

class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 题目是方阵，这里写一个不是方阵
        row = len(matrix)  # 行数
        col = len(matrix[0])  # 列数

        # 转置
        for i in range(0, row):
            for j in range(0, i):
                matrix[i][j], matrix[j][i]= matrix[j][i], matrix[i][j]

        for i in range(0, row):
            for j in range(0, col//2):
                matrix[i][j], matrix[i][col-j-1] = matrix[i][col-j-1], matrix[i][j]

        return matrix



if __name__ == '__main__':
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    solu = Solution()
    print(solu.rotate(matrix))