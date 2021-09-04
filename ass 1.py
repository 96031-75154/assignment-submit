Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 1)add two numbers
>>> a=2
>>> b=6
>>> a+b
8
>>> # 2)add integer with string
>>> a=5
>>> b="hello"
>>> a+b
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a+b
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> # 3)variable and string in one line using f string
>>> name='prashanth'
>>> print(f'{name} rapolu')
prashanth rapolu
>>> # 4)add space and new line in the print statement
>>> 'python programming language'
'python programming language'
>>> print('python\tprogramming\nlanguage')
python	programming
language
>>> 