print("File Handling")

# Read a file
f=open("files.txt")
print(f.read())
f.seek(0)
print(f.readline())
f.seek(0)
print(f.readlines(),type(f.readlines()))
f.close()

with open("files.txt") as f:
    print(f.read())
    
# Write a file


