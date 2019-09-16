#!/bin/python
# using the lambda function to get the item with the maximum weight
key_func=lambda x:x[1]

input = [[12587961, 0.7777777777777778], [12587970, 0.5172413793103449], [12587979, 0.3968253968253968], [12587982, 0.88], [12587984, 0.8484848484848485], [12587992, 0.7777777777777778], [12587995, 0.8070175438596491], [12588015, 0.4358974358974359], [12588023, 0.8985507246376812], [12588037, 0.5555555555555555], [12588042, 0.9473684210526315]]
def find_max_weight(li, key_func=None):
    default_key_func = lambda x : x
    if key_func==None:
        key_func = default_key_func
    max_value = li[0]
    for x in li:
        if key_func(x) > key_func(max_value):
            max_value=x
    return max_value

print(find_max_weight(input, key_func))

