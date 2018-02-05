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



`ord`: turn a char type into unicode code
`chr`: reverse of `ord`
`lambda`: creating anonymous function in python. Generally combined with the `map`, `filter` and `reduce` function to manipulate with collections.
```python
foo = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(map(lambda x:x * 2, foo)) # multiply by 2 for each element
print(filter(lambda x:x%2==0, foo)) # keep only the element that could be devided by 2

from functools import reduce

print(reduce(lambda x,y:x+y, foo)) # sum all the element
reduce(lambda x, y : x if x>y else y, foo) # get the maximum num inside the list
```

# Some exercise on lambda expression


```python
'''
Order Number	Book Title and Author	Quantity	Price per Item
34587	Learning Python, Mark Lutz	4	40.95
98762	Programming Python, Mark Lutz	5	56.80
77226	Head First Python, Paul Barry	3	32.95
88112	Einführung in Python3, Bernd Klein	3	24.99

Write a Python program, which returns a list with 2-tuples. Each tuple consists of a the order number and the product of the price per items and the quantity. The product should be increased by 10,- € if the value of the order is less than 100,00 €. 
Write a Python program using lambda and map.
'''
orders = [ ["34587", "Learning Python, Mark Lutz", 4, 40.95], 
	       ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
           ["77226", "Head First Python, Paul Barry", 3,32.95],
           ["88112", "Einführung in Python3, Bernd Klein", 	3, 24.99]]

result = list(map(lambda x:(x[0], x[2]*x[3] if x[2]*x[3] >= 100 else x[2]*x[3]+10), orders))
```


```python
# The same bookshop, but this time we work on a different list. The sublists of our lists look like this: 
# [ordernumber, (article number, quantity, price per unit), ... (article number, quantity, price per unit) ] 
# Write a program which returns a list of two tuples with (order number, total amount of order).
from functools import reduce

orders = [ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
	       [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
	       [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
           [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] ]

# generate the result [[1, 39.96, 233.82, 404.55], [2, 89.91, 404.55], [3, 89.91, 274.89], [4, 83.93, 208.89, 199.75]]
result = list(map(lambda x: [x[0]] + list(map(lambda y: y[1]*y[2] , x[1:])) , orders))
result = list(map(lambda x: (x[0], reduce(lambda y,z:y+z, x[1:])) , result))
result = list(map(lambda x: (x[0], x[1]) if x[1]>=100 else (x[0], x[1]), result ))
# [(1, 678.3299999999999), (2, 494.46000000000004), (3, 364.79999999999995), (4, 492.57)]
```
想象在`reduce`表达式中，每一个先前的结果的累计结果应该跟后面即将累计的item具有相同的类型。想象是在玩扑克牌的前缀累加，前面累加的结果是数字，因此可以跟后面的数字再进行累加。
```
1 2 3 4 5 6
| | | | | |
1+2
  3+3
    6+4
      10+5
         15+6
            21
```

`sorted`: sorted method is used to sort a collection. Here is the definition of sorted method `sorted(iterable, cmp=None, key=None, reverse=False)`. 
```python

```

`zip`: return an iterator of tuples.   
```python
zip('ABCD', 'xy') --> Ax By
zip([1,2,3,4], [2,3,4,5]) --> [(1,2),(2,3),(3,4),(4,5)]
zip([1,2,3,4], [2,3,4]) --> [(1,2),(2,3),(3,4)]
```

`bin`: for getting the binary of an integer

`vars`: Return the __dict__ attribute for a module, class, instance, or any other object with a __dict__ attribute corresponding to different kind of attributes inside them. For example, type `vars()` in the python console, `{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>}` will be returned.


`all`: equivalent to
```
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
```
