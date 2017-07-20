'''
we should always avoid writing for loop
'''

# list interpreter
result1 = [x * x for x in range(10)]

# list iterator
result2 = (x * x for x in range(10))

print(result1)
print(list(result2))

# lambda function
# map a seq to another seq
doubled_list = map(lambda x:x*2, range(10))

# reduce a list to an element
from functools import reduce
summation = reduce(lambda x, y : x + y, range(10))
print(summation)

# built in func
a = list(range(10))
print(a)
print(all(a))
print(any(a))
print(max(a))
print(min(a))
print(list(filter(bool, a)))
print(set(a))
print(dict(zip(a, a)))
print(sorted(a, reverse=True))
print(str(a))
print(sum(a))

# when for loop is nested in a for loop
result3 = [(i, j) for i in range(10) for j in range(i)]
print("result3:", result3)

a = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]

def max_generator(numbers):
    current_max = 0
    for i in numbers:
        current_max = max(i, current_max)
        yield current_max

print('max_generator:', list(max_generator(a)))

# use itertools when for loop required
from itertools import accumulate
results = list(accumulate(a, max))
print(results)