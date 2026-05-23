# WELCOME TO PYTHON LEARNING

`print("Hello World!")`

# Some imp points
* Indentation refers to the spaces at the beginning of a code line.

* Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.

* Python uses indentation to indicate a block of code.

* The number of spaces is up to you as a programmer, the most common use is four, but it has to be at least one.

- **A Module is a single file containing Python code (functions, classes, variables). For example, if you create a file called math_utils.py, that file is a module.**

- Library is a collection of **Modules.**

- pip is a package manager to install modules,libraries,framwork etc.

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

***Semicolons are optional in Python. You can write multiple statements on one line by separating them with `;` but this is rarely used because it makes it hard to read:***

- example

``` python
    print("Hello"); print("How are you?"); print("Bye bye!")
```

**Python prints on a new line by default.**

**Print Without a New Line
By default, the `print()` function ends with a new line.**

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
- To print text/string we can use `"` or `'`.
```python
   x = "John"
   # is the same as
   x = 'John'
```
- With the help of `type()` function we can see the variable assign data type.

**You can also use the `+` operator to output multiple variables:**
```python
   x = "Python "
   y = "is "
   z = "awesome"
   print(x + y + z)
```

**The // operator is important — in C, 7 / 2 gives 3 because both are ints. In Python, / always gives a float. Use // when you want integer division.**

**Converting between types**

`int("42")`            <!-- → 42      (string to int) -->

`float("3.14")`        <!-- → 3.14 -->

`str(100)`             <!-- '100' -->

`bool(0)`              <!-- → False   (0 is falsy, anything else is True) -->


`x=10**100`

`print(x)`  
* it is 10 to the power 100

# Data Types

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

- In Python, if a function doesn’t explicitly return anything, it returns `None` by default.

- `list` -> An ordered, mutable collection. Think of it like a dynamic array.
<!-- * Key Features:
          - Dynamic Size: You don’t need to declare the size upfront (unlike int arr[10] in C/Java). It grows/shrinks automatically.
          - Mixed Types: You can store integers, strings, and even other lists in the same list.
          - Mutable: You can change, add, or remove items after creation. -->

- `dict` -> A collection of key-value pairs. It’s implemented as a hash map under the hood.

- `tuple` -> An ordered, immutable collection. Once created, you cannot change its elements.

# I/O operations

**Input**

- To take input use `input()`.
- by default `input()` returns string so we need to change its types manually.

```python
   age=int(input("enter ur age: "))
   #for string we dont have to define the data type
```
**Output**

- To print any thint one display we use `print()`.
- `sep` and `end` are some extra parameters we can use in `print()`.
- We also use f-string to print diff data types in one line.
```python
   name="Soul"
   age=20
   percentage=79.367256
   print(f"my name is {name} and age is {age} also {percentage:.2f}")
```
- The pattern inside `{}` is always: `{value:format_spec}`. 
- Refer `format_spec` table for better under standing.
- use triple `'''`/`"""` quoates for print multiple strings in one print statement
```python
print(f"""
--- Report Card ---
Student  : {name}
Marks    : {marks:.1f} / 100
Grade    : {grade}
Result   : {"PASS" if marks >= 40 else "FAIL"}
""")
```







