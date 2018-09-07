class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        output = []
        row = [1]
        output.append(row)
        for i in range(1, numRows):
            ###basic format of a row = [1, 0, 0, ... , 0, 0, 1]
            row = [1]
            for j in range(0, i):
                row.append(0)
            row[i] = 1
            ###
            for index in range(1, i):
                row[index] = output[i-1][index]+output[i-1][index-1]
            output.append(row)
        return output
