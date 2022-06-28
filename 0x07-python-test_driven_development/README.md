# DOCTTEST — Testing Through Documentation[](https://pymotw.com/3/doctest/#module-doctest "Permalink to this headline")

Purpose:

Write automated tests as part of the documentation for a module.

`doctest`  tests source code by running examples embedded in the documentation and verifying that they produce the expected results. It works by parsing the help text to find examples, running them, then comparing the output text against the expected value. Many developers find  `doctest`  easier to use than  [`unittest`](https://pymotw.com/3/unittest/index.html#module-unittest "unittest: Automated testing framework")  because, in its simplest form, there is no API to learn before using it. However, as the examples become more complex the lack of fixture management can make writing  `doctest`  tests more cumbersome than using  [`unittest`](https://pymotw.com/3/unittest/index.html#module-unittest "unittest: Automated testing framework").

## Getting Started[](https://pymotw.com/3/doctest/#getting-started "Permalink to this headline")

The first step to setting up doctests is to use the interactive interpreter to create examples and then copy and paste them into the docstrings in the module. Here,  `my_function()`  has two examples given:

doctest_simple.py[](https://pymotw.com/3/doctest/#id1 "Permalink to this code")

def my_function(a, b):
    """
 >>> my_function(2, 3)
 6
 >>> my_function('a', 3)
 'aaa'
 """
    return a * b

To run the tests, use  `doctest`  as the main program via the  `-m`  option. Usually no output is produced while the tests are running, so the next example includes the  `-v`  option to make the output more verbose.

$ python3 -m doctest -v doctest_simple.py

Trying:
    my_function(2, 3)
Expecting:
    6
ok
Trying:
    my_function('a', 3)
Expecting:
    'aaa'
ok
1 items had no tests:
    doctest_simple
1 items passed all tests:
   2 tests in doctest_simple.my_function
2 tests in 2 items.
2 passed and 0 failed.
Test passed.

Examples cannot usually stand on their own as explanations of a function, so  `doctest`  also allows for surrounding text. It looks for lines beginning with the interpreter prompt (`>>>`) to find the beginning of a test case, and the case is ended by a blank line or by the next interpreter prompt. Intervening text is ignored, and can have any format as long as it does not look like a test case.

doctest_simple_with_docs.py[](https://pymotw.com/3/doctest/#id2 "Permalink to this code")

def my_function(a, b):
    """Returns a * b.

 Works with numbers:

 >>> my_function(2, 3)
 6

 and strings:

 >>> my_function('a', 3)
 'aaa'
 """
    return a * b

The surrounding text in the updated docstring makes it more useful to a human reader. Because it is ignored by  `doctest`, the results are the same.

$ python3 -m doctest -v doctest_simple_with_docs.py

Trying:
    my_function(2, 3)
Expecting:
    6
ok
Trying:
    my_function('a', 3)
Expecting:
    'aaa'
ok
1 items had no tests:
    doctest_simple_with_docs
1 items passed all tests:
   2 tests in doctest_simple_with_docs.my_function
2 tests in 2 items.
2 passed and 0 failed.
Test passed.

## Handling Unpredictable Output[](https://pymotw.com/3/doctest/#handling-unpredictable-output "Permalink to this headline")

There are other cases where the exact output may not be predictable, but should still be testable. For example, local date and time values and object ids change on every test run, the default precision used in the representation of floating point values depend on compiler options, and string representations of container objects like dictionaries may not be deterministic. Although these conditions cannot be controlled, there are techniques for dealing with them.

For example, in CPython, object identifiers are based on the memory address of the data structure holding the object.

doctest_unpredictable.py[](https://pymotw.com/3/doctest/#id3 "Permalink to this code")

class MyClass:
    pass

def unpredictable(obj):
    """Returns a new list containing obj.

 >>> unpredictable(MyClass())
 [<doctest_unpredictable.MyClass object at 0x10055a2d0>]
 """
    return [obj]

These id values change each time a program runs, because it is loaded into a different part of memory.

$ python3 -m doctest -v doctest_unpredictable.py

Trying:
    unpredictable(MyClass())
Expecting:
    [<doctest_unpredictable.MyClass object at 0x10055a2d0>]
****************************************************************
File ".../doctest_unpredictable.py", line 17, in doctest_unpredi
ctable.unpredictable
Failed example:
    unpredictable(MyClass())
Expected:
    [<doctest_unpredictable.MyClass object at 0x10055a2d0>]
Got:
    [<doctest_unpredictable.MyClass object at 0x1047a2710>]
2 items had no tests:
    doctest_unpredictable
    doctest_unpredictable.MyClass
****************************************************************
1 items had failures:
   1 of   1 in doctest_unpredictable.unpredictable
1 tests in 3 items.
0 passed and 1 failed.
***Test Failed*** 1 failures.

When the tests include values that are likely to change in unpredictable ways, and where the actual value is not important to the test results, use the  `ELLIPSIS`  option to tell  `doctest`  to ignore portions of the verification value.

doctest_ellipsis.py[](https://pymotw.com/3/doctest/#id4 "Permalink to this code")

class MyClass:
    pass

def unpredictable(obj):
    """Returns a new list containing obj.

 >>> unpredictable(MyClass()) #doctest: +ELLIPSIS
 [<doctest_ellipsis.MyClass object at 0x...>]
 """
    return [obj]

The “`#doctest:  +ELLIPSIS`” comment after the call to  `unpredictable()`  tells  `doctest`  to turn on the  `ELLIPSIS`  option for that test. The  `...`  replaces the memory address in the object id, so that portion of the expected value is ignored and the actual output matches and the test passes.

$ python3 -m doctest -v doctest_ellipsis.py

Trying:
    unpredictable(MyClass()) #doctest: +ELLIPSIS
Expecting:
    [<doctest_ellipsis.MyClass object at 0x...>]
ok
2 items had no tests:
    doctest_ellipsis
    doctest_ellipsis.MyClass
1 items passed all tests:
   1 tests in doctest_ellipsis.unpredictable
1 tests in 3 items.
1 passed and 0 failed.
Test passed.

There are cases where the unpredictable value cannot be ignored, because that would make the test incomplete or inaccurate. For example, simple tests quickly become more complex when dealing with data types whose string representations are inconsistent. The string form of a dictionary, for example, may change based on the order the keys are added.

doctest_hashed_values.py[](https://pymotw.com/3/doctest/#id5 "Permalink to this code")

keys = ['a', 'aa', 'aaa']

print('dict:', {k: len(k) for k in keys})
print('set :', set(keys))

Because of hash randomization and key collision, the internal key list order may be different for the dictionary each time the script runs. Sets use the same hashing algorithm, and exhibit the same behavior.

$ python3 doctest_hashed_values.py

dict: {'aa': 2, 'a': 1, 'aaa': 3}
set : {'aa', 'a', 'aaa'}

$ python3 doctest_hashed_values.py

dict: {'a': 1, 'aa': 2, 'aaa': 3}
set : {'a', 'aa', 'aaa'}

The best way to deal with these potential discrepancies is to create tests that produce values that are not likely to change. In the case of dictionaries and sets, that might mean looking for specific keys individually, generating a sorted list of the contents of the data structure, or comparing against a literal value for equality instead of depending on the string representation.

doctest_hashed_values_tests.py[](https://pymotw.com/3/doctest/#id6 "Permalink to this code")

import collections

def group_by_length(words):
    """Returns a dictionary grouping words into sets by length.

 >>> grouped = group_by_length([ 'python', 'module', 'of',
 ... 'the', 'week' ])
 >>> grouped == { 2:set(['of']),
 ...              3:set(['the']),
 ...              4:set(['week']),
 ...              6:set(['python', 'module']),
 ...              }
 True

 """
    d = collections.defaultdict(set)
    for word in words:
        d[len(word)].add(word)
    return d

The single example is actually interpreted as two separate tests, with the first expecting no console output and the second expecting the boolean result of the comparison operation.

$ python3 -m doctest -v doctest_hashed_values_tests.py

Trying:
    grouped = group_by_length([ 'python', 'module', 'of',
    'the', 'week' ])
Expecting nothing
ok
Trying:
    grouped == { 2:set(['of']),
                 3:set(['the']),
                 4:set(['week']),
                 6:set(['python', 'module']),
                 }
Expecting:
    True
ok
1 items had no tests:
    doctest_hashed_values_tests
1 items passed all tests:
   2 tests in doctest_hashed_values_tests.group_by_length
2 tests in 2 items.
2 passed and 0 failed.
Test passed.

## Tracebacks[](https://pymotw.com/3/doctest/#tracebacks "Permalink to this headline")

Tracebacks are a special case of changing data. Since the paths in a traceback depend on the location where a module is installed on the file system, it would be impossible to write portable tests if they were treated the same as other output.

doctest_tracebacks.py[](https://pymotw.com/3/doctest/#id7 "Permalink to this code")

def this_raises():
    """This function always raises an exception.

 >>> this_raises()
 Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
 File "/no/such/path/doctest_tracebacks.py", line 14, in
 this_raises
 raise RuntimeError('here is the error')
 RuntimeError: here is the error
 """
    raise RuntimeError('here is the error')

`doctest`  makes a special effort to recognize tracebacks, and ignore the parts that might change from system to system.

$ python3 -m doctest -v doctest_tracebacks.py

Trying:
    this_raises()
Expecting:
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "/no/such/path/doctest_tracebacks.py", line 14, in
      this_raises
        raise RuntimeError('here is the error')
    RuntimeError: here is the error
ok
1 items had no tests:
    doctest_tracebacks
1 items passed all tests:
   1 tests in doctest_tracebacks.this_raises
1 tests in 2 items.
1 passed and 0 failed.
Test passed.

In fact, the entire body of the traceback is ignored and can be omitted.

doctest_tracebacks_no_body.py[](https://pymotw.com/3/doctest/#id8 "Permalink to this code")

def this_raises():
    """This function always raises an exception.

 >>> this_raises()
 Traceback (most recent call last):
 RuntimeError: here is the error

 >>> this_raises()
 Traceback (innermost last):
 RuntimeError: here is the error
 """
    raise RuntimeError('here is the error')

When  `doctest`  sees a traceback header line (either “`Traceback  (most  recent  call  last):`” or “`Traceback  (innermost  last):`”, to support different versions of Python), it skips ahead to find the exception type and message, ignoring the intervening lines entirely.

$ python3 -m doctest -v doctest_tracebacks_no_body.py

Trying:
    this_raises()
Expecting:
    Traceback (most recent call last):
    RuntimeError: here is the error
ok
Trying:
    this_raises()
Expecting:
    Traceback (innermost last):
    RuntimeError: here is the error
ok
1 items had no tests:
    doctest_tracebacks_no_body
1 items passed all tests:
   2 tests in doctest_tracebacks_no_body.this_raises
2 tests in 2 items.
2 passed and 0 failed.
Test passed.

## Working Around Whitespace[](https://pymotw.com/3/doctest/#working-around-whitespace "Permalink to this headline")

In real world applications, output usually includes whitespace such as blank lines, tabs, and extra spacing to make it more readable. Blank lines, in particular, cause issues with  `doctest`  because they are used to delimit tests.

doctest_blankline_fail.py[](https://pymotw.com/3/doctest/#id9 "Permalink to this code")

def double_space(lines):
    """Prints a list of lines double-spaced.

 >>> double_space(['Line one.', 'Line two.'])
 Line one.

 Line two.

 """
    for l in lines:
        print(l)
        print()

`double_space()`  takes a list of input lines, and prints them double-spaced with blank lines between.

$ python3 -m doctest -v doctest_blankline_fail.py

Trying:
    double_space(['Line one.', 'Line two.'])
Expecting:
    Line one.
****************************************************************
File ".../doctest_blankline_fail.py", line 12, in doctest_blankl
ine_fail.double_space
Failed example:
    double_space(['Line one.', 'Line two.'])
Expected:
    Line one.
Got:
    Line one.
    <BLANKLINE>
    Line two.
    <BLANKLINE>
1 items had no tests:
    doctest_blankline_fail
****************************************************************
1 items had failures:
   1 of   1 in doctest_blankline_fail.double_space
1 tests in 2 items.
0 passed and 1 failed.
***Test Failed*** 1 failures.

The test fails, because it interprets the blank line after the line containing  `Line  one.`  in the docstring as the end of the sample output. To match the blank lines, replace them in the sample input with the string  `<BLANKLINE>`.

doctest_blankline.py[](https://pymotw.com/3/doctest/#id10 "Permalink to this code")

def double_space(lines):
    """Prints a list of lines double-spaced.

 >>> double_space(['Line one.', 'Line two.'])
 Line one.
 <BLANKLINE>
 Line two.
 <BLANKLINE>
 """
    for l in lines:
        print(l)
        print()

`doctest`  replaces actual blank lines with the same literal before performing the comparison, so now the actual and expected values match and the test passes.

$ python3 -m doctest -v doctest_blankline.py

Trying:
    double_space(['Line one.', 'Line two.'])
Expecting:
    Line one.
    <BLANKLINE>
    Line two.
    <BLANKLINE>
ok
1 items had no tests:
    doctest_blankline
1 items passed all tests:
   1 tests in doctest_blankline.double_space
1 tests in 2 items.
1 passed and 0 failed.
Test passed.

Whitespace within a line can also cause tricky problems with tests. This example has a single extra space after the  `6`.

doctest_extra_space.py[](https://pymotw.com/3/doctest/#id11 "Permalink to this code")

def my_function(a, b):
    """
 >>> my_function(2, 3)
 6 
 >>> my_function('a', 3)
 'aaa'
 """
    return a * b

Extra spaces can find their way into code via copy-and-paste errors, but since they come at the end of the line, they can go unnoticed in the source file and be invisible in the test failure report as well.

$ python3 -m doctest -v doctest_extra_space.py

Trying:
    my_function(2, 3)
Expecting:
    6
****************************************************************
File ".../doctest_extra_space.py", line 15, in doctest_extra_spa
ce.my_function
Failed example:
    my_function(2, 3)
Expected:
    6
Got:
    6
Trying:
    my_function('a', 3)
Expecting:
    'aaa'
ok
1 items had no tests:
    doctest_extra_space
****************************************************************
1 items had failures:
   1 of   2 in doctest_extra_space.my_function
2 tests in 2 items.
1 passed and 1 failed.
***Test Failed*** 1 failures.

Using one of the diff-based reporting options, such as  `REPORT_NDIFF`, shows the difference between the actual and expected values with more detail, and the extra space becomes visible.

doctest_ndiff.py[](https://pymotw.com/3/doctest/#id12 "Permalink to this code")

def my_function(a, b):
    """
 >>> my_function(2, 3) #doctest: +REPORT_NDIFF
 6 
 >>> my_function('a', 3)
 'aaa'
 """
    return a * b

Unified (`REPORT_UDIFF`) and context (`REPORT_CDIFF`) diffs are also available, for output where those formats are more readable.

$ python3 -m doctest -v doctest_ndiff.py

Trying:
    my_function(2, 3) #doctest: +REPORT_NDIFF
Expecting:
    6
****************************************************************
File ".../doctest_ndiff.py", line 16, in doctest_ndiff.my_functi
on
Failed example:
    my_function(2, 3) #doctest: +REPORT_NDIFF
Differences (ndiff with -expected +actual):
    - 6
    ?  -
    + 6
Trying:
    my_function('a', 3)
Expecting:
    'aaa'
ok
1 items had no tests:
    doctest_ndiff
****************************************************************
1 items had failures:
   1 of   2 in doctest_ndiff.my_function
2 tests in 2 items.
1 passed and 1 failed.
***Test Failed*** 1 failures.

There are cases where it is beneficial to add extra whitespace in the sample output for the test, and have  `doctest`  ignore it. For example, data structures can be easier to read when spread across several lines, even if their representation would fit on a single line.

def my_function(a, b):
    """Returns a * b.

 >>> my_function(['A', 'B'], 3) #doctest: +NORMALIZE_WHITESPACE
 ['A', 'B',
 'A', 'B',
 'A', 'B']

 This does not match because of the extra space after the [ in
 the list.

 >>> my_function(['A', 'B'], 2) #doctest: +NORMALIZE_WHITESPACE
 [ 'A', 'B',
 'A', 'B', ]
 """
    return a * b

When  `NORMALIZE_WHITESPACE`  is turned on, any whitespace in the actual and expected values is considered a match. Whitespace cannot be added to the expected value where none exists in the output, but the length of the whitespace sequence and actual whitespace characters do not need to match. The first test example gets this rule correct, and passes, even though there are extra spaces and newlines. The second has extra whitespace after  `[`  and before  `]`, so it fails.

$ python3 -m doctest -v doctest_normalize_whitespace.py

Trying:
    my_function(['A', 'B'], 3) #doctest: +NORMALIZE_WHITESPACE
Expecting:
    ['A', 'B',
     'A', 'B',
     'A', 'B',]
***************************************************************
File "doctest_normalize_whitespace.py", line 13, in doctest_nor
malize_whitespace.my_function
Failed example:
    my_function(['A', 'B'], 3) #doctest: +NORMALIZE_WHITESPACE
Expected:
    ['A', 'B',
     'A', 'B',
     'A', 'B',]
Got:
    ['A', 'B', 'A', 'B', 'A', 'B']
Trying:
    my_function(['A', 'B'], 2) #doctest: +NORMALIZE_WHITESPACE
Expecting:
    [ 'A', 'B',
      'A', 'B', ]
***************************************************************
File "doctest_normalize_whitespace.py", line 21, in doctest_nor
malize_whitespace.my_function
Failed example:
    my_function(['A', 'B'], 2) #doctest: +NORMALIZE_WHITESPACE
Expected:
    [ 'A', 'B',
      'A', 'B', ]
Got:
    ['A', 'B', 'A', 'B']
1 items had no tests:
    doctest_normalize_whitespace
***************************************************************
1 items had failures:
   2 of   2 in doctest_normalize_whitespace.my_function
2 tests in 2 items.
0 passed and 2 failed.
***Test Failed*** 2 failures.

## Test Locations[](https://pymotw.com/3/doctest/#test-locations "Permalink to this headline")

All of the tests in the examples so far have been written in the docstrings of the functions they are testing. That is convenient for users who examine the docstrings for help using the function (especially with  [`pydoc`](https://pymotw.com/3/pydoc/index.html#module-pydoc "pydoc: Online help for modules")), but  `doctest`  looks for tests in other places, too. The obvious location for additional tests is in the docstrings elsewhere in the module.

doctest_docstrings.py[](https://pymotw.com/3/doctest/#id13 "Permalink to this code")

"""Tests can appear in any docstring within the module.

Module-level tests cross class and function boundaries.

>>> A('a') == B('b')
False
"""

class A:
    """Simple class.

 >>> A('instance_name').name
 'instance_name'
 """

    def __init__(self, name):
        self.name = name

    def method(self):
        """Returns an unusual value.

 >>> A('name').method()
 'eman'
 """
        return ''.join(reversed(self.name))

class B(A):
    """Another simple class.

 >>> B('different_name').name
 'different_name'
 """

Docstrings at the module, class, and function levels can all contain tests.

$ python3 -m doctest -v doctest_docstrings.py

Trying:
    A('a') == B('b')
Expecting:
    False
ok
Trying:
    A('instance_name').name
Expecting:
    'instance_name'
ok
Trying:
    A('name').method()
Expecting:
    'eman'
ok
Trying:
    B('different_name').name
Expecting:
    'different_name'
ok
1 items had no tests:
    doctest_docstrings.A.__init__
4 items passed all tests:
   1 tests in doctest_docstrings
   1 tests in doctest_docstrings.A
   1 tests in doctest_docstrings.A.method
   1 tests in doctest_docstrings.B
4 tests in 5 items.
4 passed and 0 failed.
Test passed.

There are cases where tests exist for a module that should be included with the source code but not in the help text for a module, so they need to be placed somewhere other than the docstrings.  `doctest`  also looks for a module-level variable called  `__test__`  and uses it to locate other tests. The value of  `__test__`  should be a dictionary that maps test set names (as strings) to strings, modules, classes, or functions.

doctest_private_tests.py[](https://pymotw.com/3/doctest/#id14 "Permalink to this code")

import doctest_private_tests_external

__test__ = {
    'numbers': """
>>> my_function(2, 3)
6

>>> my_function(2.0, 3)
6.0
""",

    'strings': """
>>> my_function('a', 3)
'aaa'

>>> my_function(3, 'a')
'aaa'
""",

    'external': doctest_private_tests_external,
}

def my_function(a, b):
    """Returns a * b
 """
    return a * b

If the value associated with a key is a string, it is treated as a docstring and scanned for tests. If the value is a class or function,  `doctest`  searches them recursively for docstrings, which are then scanned for tests. In this example, the module  `doctest_private_tests_external`  has a single test in its docstring.

doctest_private_tests_external.py[](https://pymotw.com/3/doctest/#id15 "Permalink to this code")

"""External tests associated with doctest_private_tests.py.

>>> my_function(['A', 'B', 'C'], 2)
['A', 'B', 'C', 'A', 'B', 'C']
"""

After scanning the example file,  `doctest`  finds a total of five tests to run.

$ python3 -m doctest -v doctest_private_tests.py

Trying:
    my_function(['A', 'B', 'C'], 2)
Expecting:
    ['A', 'B', 'C', 'A', 'B', 'C']
ok
Trying:
    my_function(2, 3)
Expecting:
    6
ok
Trying:
    my_function(2.0, 3)
Expecting:
    6.0
ok
Trying:
    my_function('a', 3)
Expecting:
    'aaa'
ok
Trying:
    my_function(3, 'a')
Expecting:
    'aaa'
ok
2 items had no tests:
    doctest_private_tests
    doctest_private_tests.my_function
3 items passed all tests:
   1 tests in doctest_private_tests.__test__.external
   2 tests in doctest_private_tests.__test__.numbers
   2 tests in doctest_private_tests.__test__.strings
5 tests in 5 items.
5 passed and 0 failed.
Test passed.

# `UNITTEST`[](https://realpython.com/python-testing/#unittest "Permanent link")

`unittest`  has been built into the Python standard library since version 2.1. You’ll probably see it in commercial Python applications and open-source projects.

`unittest`  contains both a testing framework and a test runner.  `unittest`  has some important requirements for writing and executing tests.

`unittest`  requires that:

-   You put your tests into classes as methods
-   You use a series of special assertion methods in the  `unittest.TestCase`  class instead of the built-in  `assert`  statement

To convert the earlier example to a  `unittest`  test case, you would have to:

1.  [Import](https://realpython.com/absolute-vs-relative-python-imports/)  `unittest`  from the standard library
2.  Create a class called  `TestSum`  that inherits from the  `TestCase`  class
3.  Convert the test functions into methods by adding  `self`  as the first argument
4.  Change the assertions to use the  `self.assertEqual()`  method on the  `TestCase`  class
5.  Change the command-line entry point to call  `unittest.main()`

Follow those steps by creating a new file  `test_sum_unittest.py`  with the following code:

`import unittest

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()` 

If you execute this at the command line, you’ll see one success (indicated with  `.`) and one failure (indicated with  `F`):

`$ python test_sum_unittest.py
.F
======================================================================
FAIL: test_sum_tuple (__main__.TestSum)
----------------------------------------------------------------------
Traceback (most recent call last):
 File "test_sum_unittest.py", line 9, in test_sum_tuple
 self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")
AssertionError: Should be 6

----------------------------------------------------------------------
Ran 2 tests in 0.001s

FAILED (failures=1)` 

You have just executed two tests using the  `unittest`  test runner.

**Note:**  Be careful if you’re writing test cases that need to execute in both Python 2 and 3. In Python 2.7 and below,  `unittest`  is called  `unittest2`. If you simply  [import](https://realpython.com/python-import/)  from  `unittest`, you will get different versions with different features between Python 2 and 3.

For more information on  `unittest`, you can explore the  [unittest Documentation](https://docs.python.org/3/library/unittest.html).

#### `nose`[](https://realpython.com/python-testing/#nose "Permanent link")

You may find that over time, as you write hundreds or even thousands of tests for your application, it becomes increasingly hard to understand and use the output from  `unittest`.

`nose`  is compatible with any tests written using the  `unittest`  framework and can be used as a drop-in replacement for the  `unittest`  test runner. The development of  `nose`  as an open-source application fell behind, and a fork called  `nose2`  was created. If you’re starting from scratch, it is recommended that you use  `nose2`  instead of  `nose`.

To get started with  `nose2`, install  `nose2`  from PyPI and execute it on the command line.  `nose2`  will try to discover all test scripts named  `test*.py`  and test cases inheriting from  `unittest.TestCase`  in your current directory:

`$ pip install nose2
$ python -m nose2
.F
======================================================================
FAIL: test_sum_tuple (__main__.TestSum)
----------------------------------------------------------------------
Traceback (most recent call last):
 File "test_sum_unittest.py", line 9, in test_sum_tuple
 self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")
AssertionError: Should be 6

----------------------------------------------------------------------
Ran 2 tests in 0.001s

FAILED (failures=1)` 

You have just executed the test you created in  `test_sum_unittest.py`  from the  `nose2`  test runner.  `nose2`  offers many command-line flags for filtering the tests that you execute. For more information, you can explore the  [Nose 2 documentation](https://nose2.readthedocs.io/).

#### `pytest`[](https://realpython.com/python-testing/#pytest "Permanent link")

[`pytest`](https://realpython.com/pytest-python-testing/)  supports execution of  `unittest`  test cases. The real advantage of  `pytest`  comes by writing  `pytest`  test cases.  `pytest`  test cases are a series of functions in a Python file starting with the name  `test_`.

`pytest`  has some other great features:

-   Support for the built-in  `assert`  statement instead of using special  `self.assert*()`  methods
-   Support for filtering for test cases
-   Ability to rerun from the last failing test
-   An ecosystem of hundreds of plugins to extend the functionality

Writing the  `TestSum`  test case example for  `pytest`  would look like this:

`def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

def test_sum_tuple():
    assert sum((1, 2, 2)) == 6, "Should be 6"`
