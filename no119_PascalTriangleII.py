def getRow(rowIndex):
	row = [1]
	for i in range(rowIndex):
		row = [x + y for x, y in zip([0]+row, row+[0])]
	return row

print(getRow(0)==[1])
print(getRow(1)==[1,1])
print(getRow(2)==[1,2,1])
print(getRow(3)==[1,3,3,1])