'''
Note on https://www.youtube.com/watch?v=lYe8W04ERnY
'''

def countdown(n):
    while n > 0:
        yield n
        n-=1

for i in countdown(5):
    print(i)