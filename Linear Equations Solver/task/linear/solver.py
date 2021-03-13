from sympy import *
from sympy.solvers import solve
from sympy import Symbol
import csv
import argparse
from string import ascii_lowercase

parser = argparse.ArgumentParser()

parser.add_argument("--infile", "--infile", type=str, required=True)

parser.add_argument("--outfile", "--outfile", type=str, required=True)

args = parser.parse_args()

x = Symbol('x')
y = Symbol('y')
z = Symbol('z')

my_list = []

list_of_floats = []

my_tuple = ()

my_symbol_list = []

equation_qty_list = []

final_list = []

# print(linsolve([(x + y + z - 9), (2 * x + 4 * y - 3 * z - 1), (3 * x + 6 * y - 5 * z - 0)], (x, y, z)))

# a, b, c = map(float, input().split())
# d, e, f = map(float, input().split())
#
# temp1 = solve([(a * x) + (b * y) - c], x, y)
#
# temp2 = solve([(d * temp1[x]) + (e * y) - f], x, y)
#
# temp3 = solve([(a * x) + (b * temp2[y]) - c], x, y)
#
# print(round(float(temp3[x]),5), round(float(temp2[y]),5))

# answer = linsolve(Matrix(([1, 1, 2, 9], [2, 4, -3, 1], [3, 6, -5, 0])), (x, y, z))

with open(args.infile, "r") as in_file:
    Lines = (in_file.readlines())

for i in range(len(Lines)):
    my_list.append(Lines[i].split())

for i in range(len(my_list[0])):
    equation_qty_list.append(my_list[0][i])

equation_qty_list[0].split(" ")

variable_number = int(equation_qty_list[0])

equation_number = int(equation_qty_list[1])

# print(variable_number)
#
# print(equation_number)

my_list.pop(0)

for i in range(variable_number):
    my_symbol_list.append(Symbol((ascii_lowercase[i])))

my_symbol_list = tuple(my_symbol_list)

# for i in range(1, len(my_list)):
#     for j in range(len(my_list[0])):
#         my_list[i][j] = float(my_list[i][j])

my_tuple = tuple(my_list)

answer = linsolve(Matrix(my_tuple), my_symbol_list)

# print(answer)

# test = answer.args[0].args[0]
#
# print(test.args)
#
# m = list(test.args)
#
# print(m)
#
# m[1] = 0j
#
# test = tuple(m)
#
# print(test)

# for i in range(len(answer.args[0])):
#     try:
#         temp = (str(round(float(answer.args[0][i]), 4)))
#         print(temp)
#     except TypeError:
#         if (answer.args[0].args[0].args[1].args[1]) == I:
#             print(complex(round(answer.args[0][i])), 4)
#         else:
#             temp = answer.args[0].args[i]
#
#             temp = complex(temp)
#
#             print("%.4f+%.4fj" % (temp.real, temp.imag))
#
#         # f.write(str(round(float(answer.args[0][i]), 4)))
#         # f.write(str(round((answer.args[0][i]), 4)))
#         # f.write("\n")
#
# # print(answer.args[0][0])

with open(args.outfile, "w", encoding="utf-8") as f:
    if answer == EmptySet:
        f.write("No solutions")
        exit()
    elif len(answer.free_symbols) > 0:
        f.write("Infinitely many solutions")
        exit()
    else:
        for i in range(len(answer.args[0])):
            try:
                temp = (str(round(float(answer.args[0][i]), 4)))
                f.write(temp)
                f.write("\n")
            except TypeError:
                if (answer.args[0].args[0].args[1].args[1]) == I:
                    temp = answer.args[0].args[i]

                    temp = complex(temp)
                    print("%.4f" % (temp.real))

                    if temp.imag > 0:
                        # print("%.4f+%.4fj" % (temp.real, temp.imag))
                        final_list.append("%.4f+%.4fj" % (temp.real, temp.imag))
                        f.write(("%.4f+%.4fj " % (temp.real, temp.imag)))
                        # f.write("\n")
                    else:
                        # print("%.4f%.4fj" % (temp.real, temp.imag))
                        final_list.append("%.4f%.4fj" % (temp.real, temp.imag))
                        f.write(("%.4f%.4fj " % (temp.real, temp.imag)))
                        # f.write("\n")

                    print(final_list)

                else:
                    # f.write(str(round(float(answer.args[0][i]), 4)))
                    f.write(str(round((answer.args[0][i]), 4)))
                    f.write("\n")

        try:
            if (answer.args[0].args[0].args[1].args[1]) == I:
                f.close()
                f = open(args.outfile, "w+", encoding='utf-8')
                f.seek(0)
                # final_list.insert(0, "[")
                # final_list.append("]")
                print(final_list)
                for k in range(len(final_list)):
                    f.write(final_list[k])
                    f.write("\n")
                    # if k == 1 or k == (len(final_list)-3):
                    #     f.write(final_list[k] + " ")
                    # else:
                    #     f.write(final_list[k])

                f.close()
                # f = open(args.outfile, "a")
                # f.write("]")
                # f.close()
        except IndexError:
            exit()
