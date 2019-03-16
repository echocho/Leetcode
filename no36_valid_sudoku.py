class Solution:
	def no_duplicate_number(self, lst): 
		num_set = set()
		for item in lst:
			if item != '.':
				if item in num_set:
					return False
				num_set.add(item)
		return True

	def row_is_valid(self, board):
		return all(self.no_duplicate_number(row) for row in board)

	def col_is_valid(self, board):
		return all(self.no_duplicate_number(col) for col in zip(*board))

	def sub_box_is_valid(self, board):
		sub_box_len = 3
		return all(self.no_duplicate_number([board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]) \
			for i in (0, sub_box_len, sub_box_len+3)\
			for j in (0, sub_box_len, sub_box_len+3))


	def isValidSudoku(self, board):
		return self.row_is_valid(board) and self.col_is_valid(board) and self.sub_box_is_valid(board)

test1 = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print(Solution().isValidSudoku(test1) == False)
test2 = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print(Solution().isValidSudoku(test2) == True)
test3 = [[".",".",".",".","5",".",".","1","."],
         [".","4",".","3",".",".",".",".","."],
         [".",".",".",".",".","3",".",".","1"],
         ["8",".",".",".",".",".",".","2","."],
         [".",".","2",".","7",".",".",".","."],
         [".","1","5",".",".",".",".",".","."],
         [".",".",".",".",".","2",".",".","."],
         [".","2",".","9",".",".",".",".","."],
         [".",".","4",".",".",".",".",".","."]]
print(Solution().isValidSudoku(test3) == False)