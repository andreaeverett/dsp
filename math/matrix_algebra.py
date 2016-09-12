# Matrix Algebra

from numpy import matrix
from numpy import linalg

A = matrix([[1, 2, 3],[2, 7, 4]])
B = matrix([[1, -1],[0, 1]])
C = matrix([[5, -1],[9, 1],[6, 0]])
D = matrix([[3, -2, -1], [1, 2, 3]])
u = matrix([[6, 2, -3, 5]])
v = matrix([[3, 5, -1, 4]])
w = matrix([[1],[8],[0],[5]])


# Part 1.
# My calculation 1.1 : 2 x 3
print A.shape # Python returns (2, 3)

#  My calculation 1.2 : 2 x 2
print B.shape # Python returns (2, 2)

#  My calculation 1.3 : 3 x 2
print C.shape # Python returns (3, 2)

#  My calculation 1.4 : 2 x 3
print D.shape # Python returns (2, 3)

#  My calculation 1.5 : 1 x 4
print u.shape # Python returns (1, 4)

#  My calculation 1.6 : 4 x 1
print w.shape # Python returns (4, 1)

# Part 2.
#  My calculation 2.1 : u + v = [9 7 -4 9]
print u + v # Python returns [[ 9  7 -4  9]]

#  My calculation 2.2 : u - v = [3 -3 -2 1]
print u - v # Python returns [[ 3 -3 -2  1]]

#  My calculation 2.3 : 6u = [36 12 -18 30]
print 6*u # Python returns [[ 36  12 -18  30]]

#  My calculation 2.4 : u*v = Not defined
# print u*v # Python returns "ValueError: shapes (1,4) and (1,4) not aligned: 4 (dim 1) != 1 (dim 0)"

#  My calculation 2.5 : ||u|| = sqrt(74) = 8.602325267042627
print linalg.norm(u) # Python returns 8.60232526704

# Part 3.
#  My calculation 3.1 : A + C is not defined
print A + C # Python returns "ValueError: operands could not be broadcast together with shapes (2,3) (3,2)"

#  My calculation 3.2 : A - C^T = [[-4 -7 -3], [3 6 4]]
print A - C.T
# Python returns:
#[[-4 -7 -3]
# [ 3  6  4]]

#  My calculation 3.3 : C^T + 3D = [[14 3 3], [2 7 9]]
print C.T + 3*D
# Python returns:
#[[14  3  3]
# [ 2  7  9]]


#  My calculation 3.4 : BA = [[-1 -5 -1], [2 7 4]]
print B*A
# Python returns:
#[[-1 -5 -1]
# [ 2  7  4]]


#  My calculation 3.5 : BA^T is not defined
print B* A.T # Python returns "ValueError: shapes (2,2) and (3,2) not aligned: 2 (dim 1) != 3 (dim 0)"

#  My calculation 3.6 : BC is not defined
print B*C # Python returns "ValueError: shapes (2,2) and (3,2) not aligned: 2 (dim 1) != 3 (dim 0)"

#  My calculation 3.7 : CB = [[5 -6], [9 -8], [6 -6]]
print C*B
# Python returns:
#[[ 5 -6]
# [ 9 -8]
# [ 6 -6]]


#  My calculation 3.8 : B^4 = [[1 -4], [0 1]]
print B**4
# Python returns:
#[[ 1 -4]
# [ 0  1]]


#  My calculation 3.9 : AA^T = [[14 28], [28 69]
print A*A.T
# Python returns:
#[[14 28]
# [28 69]]


#  My calculation 3.10 : (D^T)D = [[10 -4 0], [-4 8 8 ], [0 8 10]]
print D.T*D
# Python returns:
#[[10 -4  0]
# [-4  8  8]
# [ 0  8 10]]
