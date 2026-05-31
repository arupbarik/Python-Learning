print("Dictionaries")

student={
    "name":"john",
    "age":18,
    "SGPA":8
}
empty={}
also_empty=dict()
print(student["name"])

student["name"]="alice"
print(student["name"])
print(len(student))
print(type(student))

new=dict(name="Dhoni",team="CSK")
print(new["name"])

x=new.get("team")
print(x)

#Before chnage
x=new.keys()
print(x)

#after change
new["num"]=7
x=new.keys()
print(x)

#Before chnage
x=new.values()
print(x)

#after change
new["num"]=7.0
x=new.values()
print(x)

print(new.items())

if "num" in new:
    print("YES")
