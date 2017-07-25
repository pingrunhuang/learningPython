## Built in function
* The built-in function dir() is used to find out which names a module defines
* `zip()`:  in conjunction with the * operator can be used to unzip a list:
```python
x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y)
list(zipped)
[(1, 4), (2, 5), (3, 6)]
x2, y2 = zip(*zip(x, y))
x == list(x2) and y == list(y2)
True
```

