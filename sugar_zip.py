matrix = [
    [ 1, 2, 3 ],
    [ 8, 9, 4 ],
    [ 7, 6, 5 ]
]
# 
t1 = zip(matrix)
for x in t1:
    print(x)

# combine element in the corresponding index  
t2 = zip(*matrix)
for x in t2:
    print(x)

t3 = [*zip(*matrix)]
print(t3)