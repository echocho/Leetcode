class Solution:
	def has_duplicate_number(self, lst): 
		num_set = set()
		for item in lst:
			if item != '.':
				if item in num_set:
					return True
				num_set.add(item)
		return False

	def row_is_valid(self, board):
		for row in board:
			if self.has_duplicate_number(row):
				return False
		return True

	def col_is_valid(self, board):
		for col in zip(*board):
			if self.has_duplicate_number(col):
				return False
		return True 

	def sub_box_is_valid(self, board):
		for i in (0, 3, 6):
			for j in (0, 3, 6):
				sub_box = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
				if self.has_duplicate_number(sub_box):
					return False
		return True

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