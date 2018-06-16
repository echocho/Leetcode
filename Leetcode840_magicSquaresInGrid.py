# Leetcode840_magicSquaresInGrid.py

def numMagicSquaresInside(grid):
    
    i = 0 
    count = 0
    while i+3 <= len(grid[0]):
        print('i', i)
        row_a, row_b, row_c = grid[0][i:i+3], grid[1][i:i+3], grid[2][i:i+3]
        print('row_a= ', row_a)
        print('row_b= ', row_b)
        print('row_c= ', row_c)
        if row_a[0]+row_b[1]+row_c[2] == row_a[2]+row_b[1]+row_c[0] == sum(row_a) == sum(row_b) == sum(row_c) == row_a[0]+row_b[0]+row_c[0] == row_a[1]+row_b[1]+row_c[1] == row_a[2]+row_b[2]+row_c[2]:
            print('true')
            count += 1
            print('count= ', count)
        i += 1
        print('new i= ', i)
    return count

# print(numMagicSquaresInside([[4,3,8,4],
#         [9,5,1,9],
#         [2,7,6,2]]))
print(numMagicSquaresInside([[1,10,3,5],[1,1,6,11],[1,7,9,2]]))
print(numMagicSquaresInside([[10,3,5],[1,6,11],[7,9,2]]))
