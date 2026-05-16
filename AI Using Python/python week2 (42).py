# using context managers (with statement)
# ye isliye use hta ke isme hm python ko bataty hy ke hm file ko itny time
# ke liye sue ker ry uske bad python automatically us file ko close kerdega
# ab jasy hy ye code sy bhr ayengy file automaticaly close hojaega
with open("nommi.txt","r") as file:
    data=file.read()
    print(data)
# now file close automatically closed