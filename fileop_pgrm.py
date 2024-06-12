import os
f=open("myfile.txt","r")
#f.write("hello world!")
print(f.read())
f.close()

os.remove("myfile.txt")