# loops----> repetiontion of things
# for loop---. is  used to know exactly how many times to repeat

# colors=("red","green","yellow","purple")
# for i in colors:
#     print(i)
#
#
# nmb=10
# for i in range(1,10):
#     print(i)
#
#
# for i in range(4):
#     x=int(input("enter a number"))
#     if 1<=x<=100:
#         print("valid no")
#         break
#     else:
#         print("invalid try again")
#
#
# for i in range(4):
#     print("python is fun")
#
# for char in "python":
#     print(char)

# i=5
# rows=i
# cols=i
# matrix=[]
# for i in range(rows):
#     row=[]
#     for c in range(cols):
#          row.append(0)
#     matrix.append(row)
# for row in matrix:
#     print(' '.join(map(str,row)))

# i=4
# rows=i

# rows=5
# for level in range(1,rows+1):
#     print(' ' * (rows-level)+ '*' *(2*level-1))

# for reverse
rows = 5
for level in range(rows, 0, -1):
    print(' ' * (rows - level) + "*" * (2 * level - 1))