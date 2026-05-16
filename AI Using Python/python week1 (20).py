#for  nested loop
for i in range(3):
    print("outer loop")
    for j in range(3):
        print("inner loop")


i=4
rows=i
cols=i
matrix=[]
for i in range(rows):
    row=[]
    for c in range(cols):
        row.append(0)
    matrix.append(row)
for row in matrix:
    print(' ' .join(map(str,row)))



# table banana
number=int(input("enter number: "))
for i in range(1,11):
    print(f"{number} *{i}={number*i}")
