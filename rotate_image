class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        temp
        row, col
        new_col = length - row + 1
        new_row = col
        
        #one row에 대해 실행하자
        #temp = matrix[0][0]
        #matrix[0][0] = matrix[to row[final]
        #
        length = len(matrix[0])
        for row in range(0, int(length/2)):
            for col in range(row, length-row-1):
                temp = matrix[col][length-row-1]
                matrix[col][length-row-1] = matrix[row][col]
                matrix[row][col] = matrix[length-col-1][row]
                matrix[length-col-1][row] = matrix[length-row-1][length-col-1]
                matrix[length-row-1][length-col-1] = temp
                print(matrix)
        """
        matrix[::] = zip(*matrix[::-1])
