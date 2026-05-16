# handling exceptions during file operation
# common issues in file handling
# 1-->file not found
# 2-->wrong path
# 3-->wrong file mode
# to solve it is exception handling
# with open("missing.text","r") as file:
#     print(file.read())

try:
    with open("missing.text","r") as file:
        print(file.read())
except FileNotFoundError:
    print("file not found")

#try to read existing file,if missing,create it with name and age,then read
filename="my_info.text"
name="copilot"
age=78
try:
    with open(filename,"r") as fin:
        print(fin.read())
except FileNotFoundError:
    with open(filename,"w") as fout:
        fout.write(f"{name}\n{age}\n")
    with open(filename,"r") as fout:
        print(fout.read())
