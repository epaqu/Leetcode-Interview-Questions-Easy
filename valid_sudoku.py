class Solution(object):
    def isValidSudoku(self, board):
        #check row by row for duplicates
        for row in board:
            nums = filter(lambda a: a != ".", row)
            if len(set(nums)) != len(nums):
                return False
        # check col by col for duplicates
        for col in range(0,9):
            nums = []
            for row in range(0,9):
                nums.append(board[row][col])
            nums = filter(lambda a: a != ".", nums)
            if len(set(nums)) != len(nums):
                return False
        # int(i/3), int(j/3)번째 스퀘어에서 unique
            # i = [int(i/3)*3:int(i/3)*3+3]
            # j = [int(j/3)*3:int(j/3)*3+3]
            # 에서 유니크해야함
        for row in range(0,3):
            for col in range(0,3):
                nums = []
                square = board[row*3:row*3+3]
                nums.extend(square[0][col*3:col*3+3])
                nums.extend(square[1][col*3:col*3+3])
                nums.extend(square[2][col*3:col*3+3])
                nums = filter(lambda a: a != ".", nums)
                if (len(set(nums)) != len(nums)):
                    return False
        return True
