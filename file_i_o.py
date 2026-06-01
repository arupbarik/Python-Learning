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
with open("files.txt", "a") as f:
    f.write("now a line.")

with open("files.txt") as f:
    print(f.read())

with open("files.txt", "w") as f:    # it overwrites the file content
    f.write("hmmm")
with open("files.txt") as f:
    print(f.read())
