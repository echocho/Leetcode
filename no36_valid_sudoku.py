from collections import Counter
sodoku = [
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

def has_duplicate_number(dictionary):
	if any([v > 1 for k, v in digits.items() if k != '.']):
		return True
	return False

for row in sodoku:
	digits = Counter(row)
	if has_duplicate_number(digits):
		print('row wrong')

for col in zip(*sodoku):
	digits = Counter(col)
	if has_duplicate_number(digits):
		print('col wrong')

start, end = 0, 9
cnt_left = 3
# while i <= 9 and j <= 9:
sub_box = [sodoku[i][j] for i in range(0, )]
