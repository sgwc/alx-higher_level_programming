# 7. Input and Output[](https://docs.python.org/3/tutorial/inputoutput.html#input-and-output "Permalink to this headline")

There are several ways to present the output of a program; data can be printed in a human-readable form, or written to a file for future use. This chapter will discuss some of the possibilities.

## 7.1. Fancier Output Formatting[](https://docs.python.org/3/tutorial/inputoutput.html#fancier-output-formatting "Permalink to this headline")

So far we’ve encountered two ways of writing values:  _expression statements_  and the  [`print()`](https://docs.python.org/3/library/functions.html#print "print")  function. (A third way is using the  `write()`  method of file objects; the standard output file can be referenced as  `sys.stdout`. See the Library Reference for more information on this.)

Often you’ll want more control over the formatting of your output than simply printing space-separated values. There are several ways to format output.

-   To use  [formatted string literals](https://docs.python.org/3/tutorial/inputoutput.html#tut-f-strings), begin a string with  `f`  or  `F`  before the opening quotation mark or triple quotation mark. Inside this string, you can write a Python expression between  `{`  and  `}`  characters that can refer to variables or literal values.
    
    >>>
    
    >>> year = 2016
    >>> event = 'Referendum'
    >>> f'Results of the {year}  {event}'
    'Results of the 2016 Referendum'
    
-   The  [`str.format()`](https://docs.python.org/3/library/stdtypes.html#str.format "str.format")  method of strings requires more manual effort. You’ll still use  `{`  and  `}`  to mark where a variable will be substituted and can provide detailed formatting directives, but you’ll also need to provide the information to be formatted.
    
    >>>
    
    >>> yes_votes = 42_572_654
    >>> no_votes = 43_132_495
    >>> percentage = yes_votes / (yes_votes + no_votes)
    >>> '{:-9} YES votes {:2.2%}'.format(yes_votes, percentage)
    ' 42572654 YES votes  49.67%'
    
-   Finally, you can do all the string handling yourself by using string slicing and concatenation operations to create any layout you can imagine. The string type has some methods that perform useful operations for padding strings to a given column width.
    

When you don’t need fancy output but just want a quick display of some variables for debugging purposes, you can convert any value to a string with the  [`repr()`](https://docs.python.org/3/library/functions.html#repr "repr")  or  [`str()`](https://docs.python.org/3/library/stdtypes.html#str "str")  functions.

The  [`str()`](https://docs.python.org/3/library/stdtypes.html#str "str")  function is meant to return representations of values which are fairly human-readable, while  [`repr()`](https://docs.python.org/3/library/functions.html#repr "repr")  is meant to generate representations which can be read by the interpreter (or will force a  [`SyntaxError`](https://docs.python.org/3/library/exceptions.html#SyntaxError "SyntaxError")  if there is no equivalent syntax). For objects which don’t have a particular representation for human consumption,  [`str()`](https://docs.python.org/3/library/stdtypes.html#str "str")  will return the same value as  [`repr()`](https://docs.python.org/3/library/functions.html#repr "repr"). Many values, such as numbers or structures like lists and dictionaries, have the same representation using either function. Strings, in particular, have two distinct representations.

Some examples:

>>>

>>> s = 'Hello, world.'
>>> str(s)
'Hello, world.'
>>> repr(s)
"'Hello, world.'"
>>> str(1/7)
'0.14285714285714285'
>>> x = 10 * 3.25
>>> y = 200 * 200
>>> s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
>>> print(s)
The value of x is 32.5, and y is 40000...
>>> # The repr() of a string adds string quotes and backslashes:
... hello = 'hello, world\n'
>>> hellos = repr(hello)
>>> print(hellos)
'hello, world\n'
>>> # The argument to repr() may be any Python object:
... repr((x, y, ('spam', 'eggs')))
"(32.5, 40000, ('spam', 'eggs'))"

The  [`string`](https://docs.python.org/3/library/string.html#module-string "string: Common string operations.")  module contains a  [`Template`](https://docs.python.org/3/library/string.html#string.Template "string.Template")  class that offers yet another way to substitute values into strings, using placeholders like  `$x`  and replacing them with values from a dictionary, but offers much less control of the formatting.

### 7.1.1. Formatted String Literals[](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals "Permalink to this headline")

[Formatted string literals](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)  (also called f-strings for short) let you include the value of Python expressions inside a string by prefixing the string with  `f`  or  `F`  and writing expressions as  `{expression}`.

An optional format specifier can follow the expression. This allows greater control over how the value is formatted. The following example rounds pi to three places after the decimal:

>>>

>>> import math
>>> print(f'The value of pi is approximately {math.pi:.3f}.')
The value of pi is approximately 3.142.

Passing an integer after the  `':'`  will cause that field to be a minimum number of characters wide. This is useful for making columns line up.

>>>

>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
>>> for name, phone in table.items():
...     print(f'{name:10} ==> {phone:10d}')
...
Sjoerd     ==>       4127
Jack       ==>       4098
Dcab       ==>       7678

Other modifiers can be used to convert the value before it is formatted.  `'!a'`  applies  [`ascii()`](https://docs.python.org/3/library/functions.html#ascii "ascii"),  `'!s'`  applies  [`str()`](https://docs.python.org/3/library/stdtypes.html#str "str"), and  `'!r'`  applies  [`repr()`](https://docs.python.org/3/library/functions.html#repr "repr"):

>>>

>>> animals = 'eels'
>>> print(f'My hovercraft is full of {animals}.')
My hovercraft is full of eels.
>>> print(f'My hovercraft is full of {animals!r}.')
My hovercraft is full of 'eels'.

For a reference on these format specifications, see the reference guide for the  [Format Specification Mini-Language](https://docs.python.org/3/library/string.html#formatspec).
