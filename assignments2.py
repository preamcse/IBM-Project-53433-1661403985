Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> mylist=[4,7,3,8,1,5,9]
>>> print(mylist)
[4, 7, 3, 8, 1, 5, 9]
>>> mylist(0)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    mylist(0)
TypeError: 'list' object is not callable
>>> mylist[0]
4
>>> mylist[0]=2
>>> print(mylist)
[2, 7, 3, 8, 1, 5, 9]
>>> mylist.remove(3)
>>> print(mylist)
[2, 7, 8, 1, 5, 9]
>>> mylist.append(5)
>>> print(mylist)
[2, 7, 8, 1, 5, 9, 5]
>>> mylist.sort()
>>> print(mylist)
[1, 2, 5, 5, 7, 8, 9]
>>> mylist.pop(5)
8
>>> mylis.reverse()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    mylis.reverse()
NameError: name 'mylis' is not defined. Did you mean: 'mylist'?
>>> mylist.reverse()
>>> print(mylist)
[9, 7, 5, 5, 2, 1]
