# Some imp points
* Indentation refers to the spaces at the beginning of a code line.

* Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.

* Python uses indentation to indicate a block of code.

* The number of spaces is up to you as a programmer, the most common use is four, but it has to be at least one.

# Example

``` python
    if 5 > 2:
     print("Five is greater than two!")
```
# Wrong code

``` python
    if 5 > 2:
    print("Five is greater than two!")
```

***Semicolons are optional in Python. You can write multiple statements on one line by separating them with ; but this is rarely used because it makes it hard to read:***

- example

``` python
    print("Hello"); print("How are you?"); print("Bye bye!")
```

**Python prints on a new line by default.**

**Print Without a New Line
By default, the print() function ends with a new line.**

**If you want to print multiple words on the same line, you can use the end parameter:**

``` python
    print("Hello World!", end=" ")
    print("I will print on the same line.")
```

# Mix Text and Numbers
You can combine text and numbers in one output by separating them with a comma:

``` python
    print("I am", 35, "years old.")
```
# Variables
- Variables are case sensitive 
- To print text/string we can use " or '.
```python
   x = "John"
   # is the same as
   x = 'John'
```
- With the help of `type()` function we can see the variable assign data type.

**You can also use the + operator to output multiple variables:**
```python
   x = "Python "
   y = "is "
   z = "awesome"
   print(x + y + z)
```

| Type | Examples |
| --- | --- |
| Text Type | str |
| Numeric Types | int, float, complex |
| Sequence Types | list, tuple, range |
| Mapping Type | dict |
| Set Types | set, frozenset |
| Boolean Type | bool |
| Binary Types | bytes, bytearray, memoryview |
| None Type | NoneType |

**The // operator is important — in C, 7 / 2 gives 3 because both are ints. In Python, / always gives a float. Use // when you want integer division.**

**Casting**

