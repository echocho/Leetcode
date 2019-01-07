# solution 1: OK. This is not the right way to do it 
class Solution1:
	def addBinary(self, a, b):
		return bin(int(a,2) + int(b,2))[2:]

# solution 2: calculate by using 2's square
class Solution2:
	def addBinary(self, a, b):
		A, B = 0, 0
        a, b = a[::-1], b[::-1]
        for i in range(len(a)):
            A = A + 2 ** i * int(a[i])
        for j in range(len(b)):
            B = B + 2 ** j * int(b[j])
        return bin(A + B)[2:]
        