from display import *
from draw import *
from matrix import *

### TEST CODE
# m1 = new_matrix()
# print_matrix(m1)
#
# m1_rows = len(m1[0])
# m1_columns = len(m1)
#
# for i in range(m1_rows):
#     for j in range(m1_columns):
#         m1[i][j] = i + j
#
# print_matrix(m1)
#
# m2 = new_matrix()
# ident(m2)
# print_matrix(m2)
#
#
# m3 = matrix_mult(m1,m2)
# print_matrix(m3)
#
# m4 = matrix_mult(m1,m1)
# print_matrix(m4)


screen = new_screen()
color_red = [ 255, 0, 0 ]
color_green = [ 0, 255, 0 ]
color_blue = [ 0, 0, 255 ]
m1 = new_matrix()

i = 3
m1 = add_edge(m1, 25 * i, 50, 0, 25 * (i + 7), 400, 0)
m1 = add_edge(m1, 25 * (i + 7), 400, 0, 25 * (i + 12), 50, 0)
m1 = add_edge(m1, 25 * (i + 12), 50, 0, 25 * (i -1), 300, 0)
m1 = add_edge(m1, 25 * (i -1), 300, 0, 25 * (i + 13), 300, 0)
m1 = add_edge(m1, 25 * (i + 13), 300, 0, 25 * i, 50, 0,)
draw_lines(m1, screen, color_blue)

# i = 3
# while i < 5:
#     m1 = add_edge(m1, 25 * i, 50, 0, 25 * (i + 7), 400, 0)
#     m1 = add_edge(m1, 25 * (i + 7), 400, 0, 25 * (i + 12), 50, 0)
#     m1 = add_edge(m1, 25 * (i + 12), 50, 0, 25 * (i -1), 300, 0)
#     m1 = add_edge(m1, 25 * (i -1), 300, 0, 25 * (i + 13), 300, 0)
#     m1 = add_edge(m1, 25 * (i + 13), 300, 0, 25 * i, 50, 0,)
#     draw_lines(m1, screen, color_blue)
#     i += 1




display(screen)
save_ppm(screen, 'binary.ppm')
save_ppm_ascii(screen, 'ascii.ppm')
save_extension(screen, 'img.png')
