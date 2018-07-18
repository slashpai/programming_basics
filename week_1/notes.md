## What is a computer program?

A computer program is a set of instructions written to solve a problem by computer. Read more [here](https://en.wikipedia.org/wiki/Computer_program)

## What are different types of computer programs?

Based on functionalities, we can categorize programs as mainly system programs, application programs etc. Example for system programs are operating systems which provides environment for application programs to execute in efficient way. Compilers are another example for system programs. Application programs are designed for a specific purpose. Example for application programs are MS Office, Media player etc.

## Compiled vs Interpretted language

Compiled language will convert the program into machine understandable instructions before being saved as executable. Examples for compiled languages are C, C++ etc.Interpretted language will save the code same format as you entered and they gets converted to machine understandable during run time. Examples for interpretted languages are python, ruby etc.There is a good explanation [here](https://www.upwork.com/hiring/development/the-basics-of-compiled-languages-interpreted-languages-and-just-in-time-compilers/)

## What are keywords?

Keywords are the reserved words which has a specific meaning in language. They are case sensitive.

## What are Identifiers?

Identifier is the name given to entities like class, functions, variables etc. They are used to differentiate between each entities

## Basic syntax

Most of the programming languages use { and } to define a code block where as in python,  indendation is used for that. The amount of indendation can be anything but that must be same through out the block. 4 spaces are the standard used. Since python enforces the indendation which is not by other languages your code will look neat and readable. Refer [style guide](https://www.python.org/dev/peps/pep-0008/) for styles used in python

`#` is used to comment any line in python. If there are multiple line you can use ''' or """

`#` This is a comment in python
'''This is a multiline
comment in python'''

* Variable types

A variable is a named location in memory where data is stored. We don't assign values to variables in Python, but reference of value to variable. You don't have to declare a variable specifically as int, float, string etc. Based on value assigned to the varible its data type will be decided in python.

Integer types: Integer numbers

```python
num = 5
```

Float types: Numbers with decimal points

```python
num = 5.2
```

String Types: Group of characters

```python
str = "Hello World!"
```

You can use either single quotes or double quotes in Python to represent string. If there is a single quotes involved in your string itself you can use `"` to wrap it or you have to escape the quotes in string

```python
str = "He's a good boy"
str = 'He\'s a good boy'
```

Constant: A type of variable whose value cannot be changed. Their value cannot be changed throughout the execution of program.

```python
PI = 3.14
```

* Operators

I have listed only main operators in this section. Please read more [here](https://www.geeksforgeeks.org/basic-operators-python/)

**Arithmetic Operators:**  **, %, //, /, *, + , -

| Operator| Desc |Example |
--|--|--|
**| Exponent|2 ** 3 = 8|
%| Modulus|10 % 3 = 1|
//| Integer Division|3 // 2 = 1|
/| Float Division|3 / 2 = 1.5|
*| Multiplication|2 * 3 = 6|
+| Sum|2 + 3 = 5|

**Relational Operators:** <, >, <=, >=, ==, !=

| Operator| Desc |Example |
--|--|--|
<| less than|2 < 3 => True|
\>| greater than|10 > 3 => True|
\>=| greater than equal to| 2 >= 5 => False|
<=| less than equal to |2 <= 3 => True|
==| equality|2 == 3 => False|
!=| Inquality|2 != 3 => True|

**Logical Operators:** not, and, or

| Operator| Desc |Example |
--|--|--|
|not| True if operand is false and vice versa | a = True, not a => False|
|and| True if both operands are True | a = True, b = False, a and b => False|
|or| True if either of operands is True | a = True, b = False, a or b => True|

* Decision making

Normally the computer executes the program in the same order its written. But if you want the statements to be executed only when a certain condition satifies you have to use conditional or decision making statements

**if..else:** When you have only one or two conditions to evaluate

```python
num = 5
if num % 2 == 0:
    print("Even number")
else:
    print ("Odd number")
```

**if..elif..else:** When you have more than two conditions to evaualate. Which ever if statement is satified only that will be executed. In below example, it will be printed `Average score` when executed. Try by setting different score in `cricket_score` variable and execute. Make sure code is indented when its pasted else you will get error in python interpretter

```python
cricket_score = 250
if cricket_score < 100:
    print("Poor score")
elif cricket_score >= 100 and cricket_score <= 250:
    print ("Average score")
elif cricket_score > 250 and cricket_score <= 300:
    print ("Good score")
else:
    print ("Outstanding score")
```

* Practice in [python shell](https://www.python.org/shell/)
