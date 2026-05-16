# modes of file handling--->read,write & append
import fileinput

file1=open("nommi.txt","r")
print(file1.read())
file1.close()

file1=open("nommi.txt","w")
file1.write("this is another test")
file1.close()

file1=open("nommi.txt","a")
file1.write("\n this is happen during parctic")
file1.close()