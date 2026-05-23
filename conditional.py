print("conditional statement")
# programme for find out odd and even numbers
print("Enter ur number:")
num=int(input())
if num%2==0:
    print("It is a Even number")
else:
    print("It is a Odd number")

# greatest among three numbers
print("Enter num")
a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    print(f"{a} is greater among {a} {b} {c}")
elif b>c:
    print(f"{b} is greater among {a} {b} {c}")
elif a==b==c:
    print("All are equal")
else:
    print(f"{c} is greater among {a} {b} {c}")
# print name of days with match
day=4
match day:
    case 1:
        print("Monday")
    case 2:
        print("tuesday")
    case 3:
        print("wedsnes day")
    case 4:
        print("thrusday")
    case 5:
        print("friday")
    case 6:
        print("saturday")
    case 7:
        print("sunday")
