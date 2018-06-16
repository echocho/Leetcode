# Leetcode476_numberComplement.py

def findComplement(num):
    bin_num = bin(num)
    elems = []
    for i in bin_num[2:]:
        i = int(i) ^ 1
        elems.append(str(i))
    str_comp = ''.join(elems)
    return int(str_comp, 2)

print(findComplement(5) == 2)
print(findComplement(1) == 0)
