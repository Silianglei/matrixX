"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    s = ""
    current_spaces = 7
    for c in range(4):
        s += "\n"
        for r in range(len(matrix)):
            s += str(matrix[r][c])
            # if current_spaces < how_manyDigits(matrix[r][c]):
            #     current_spaces += 1
            for i in range(current_spaces - how_manyDigits(matrix[r][c])):
                s += " "
    s += "\n"
    print(s)

def how_manyDigits(n):
    if (n == 0):
        return 1
    i = 0
    number_of_digits = 0
    for i in range(10):
        if (10 ** i) <= n:
            number_of_digits += 1
    return number_of_digits

    # for rows in matrix:
    #     print(rows)

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    columns = len(matrix[0])
    rows = columns #matrix is assumed to be a square
    for r in range(rows):
        for c in range(columns):
            if (r == c):
                matrix[r][c] = 1
            else:
                matrix[r][c] = 0
    return matrix

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2


def matrix_mult( m1, m2 ):
    m2_clone = new_matrix()
    columns = len(m2[0])
    for r in range(4):
        for c in range(columns):
            m2_clone[r][c] = m2[r][c]
    for r in range(4):
        for c in range(columns):
            m2[r][c] = (m1[r][0] * m2_clone[0][c]) + (m1[r][1] * m2_clone[1][c]) + (m1[r][2] * m2_clone[2][c]) + (m1[r][3] * m2_clone[3][c])
    return m2


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
