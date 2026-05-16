# reading from & writing to files in python-->concept of file handling
# text file--->contain simple,human readable data
# CSV--->comma separted value: a data is stored in tabular form separated by comma
# web applicatiion-->commonly use json format for structure data exchange
#
file=open("nommi.txt","r")
print(file.read())
file.close()

file=open("nommi.txt","w")
file.write("this is another data of me")
file.close()

# append is use for added data and the old is remain also
file=open("nommi.txt","a")
file.write("\n new line added!")
file.close()