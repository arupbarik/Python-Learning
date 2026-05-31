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

# Modification
detail={
    "name":"adam",
    "age":18,
    "ID":152858,
    "Region":"USA"
}
print(detail)

detail.update({"age":24})
print(detail)

detail["Hobby"]="Gaming"
print(detail)

detail.update({"Occupation":"Student"})
print(detail)

detail.pop("Occupation")
print(detail)

detail.popitem()
print(detail)

del detail["ID"]
print(detail)

detail.clear()
print(detail)

#Copy dict
thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

mydict = thisdict.copy()
print(mydict)

new_dict=dict(thisdict)
print(new_dict)

#nested
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily["child2"]["name"])

for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])