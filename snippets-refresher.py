# EPIP (Elements of Programming Interviews in Python)
# Code Snippets Cheet Sheet if you just have 10 minutes
# TODO: refresh/skim before coding interview at FAANG (Facebook, Apple, Amazon, Netflix, Google)
# Created by Sergei Panarin, software engineer, author of The $100K Engineer blog
# http://the100kengineer.substack.com/?utm_source=github&utm_medium=snippets

# TABLE OF CONTENTS (TOC):
# 1. BASICS
# 2. LOOPS
# 3. LIST PROCESSING
# 4. CONDITIONS
# 5. TUPLES
# 6. HEAP


# 1. BASICS
print('-'*30, 'BASICS', '-'*30)
# 1.1 SHORTCUTS
# value swap
a, b = 1, 2 # a=1, b=2
a, b = b, a # a=2, b=1
# tuple unpacking
x, y = (1, 2) # x=1, y=2
# list unpacking
a, b, c = [1, 2, 3] # a=1, b=2, c=3
# dictionary unpacking
d = {'a': 1, 'b': 2, 'c': 3}
a, b, c = d.values() # a=1, b=2, c=3

# 1.2 ARITHMETIC
print(10 / 3) # 3.3333333333333335 - true division
print(10 // 3) # 3 - floor division (integer division)
print(10 % 3) # 1 - modulus (the remainder of the division)
print(10 ** 3) # 1000 - exponentiation

# 1.3 MIN/MAX
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(min(a)) # 1
print(max(a)) # 10

# 1.4 LAMBDA FUNCTIONS (anonymous functions)
f = lambda arg1, arg2: arg1 * arg2
print(f(2, 3)) # 6

# 1.5 TERNARY OPERATOR (like in JavaScript "condition ? value_if_true : value_if_false")
n = 3
res = "Even" if n % 2 == 0 else "Odd"
print(res) # "Odd"

# 2. LOOPS (lists, dictionaries, sets)
print('-'*30, 'LOOPS', '-'*30)
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list 
for item in a:
    print(item, end=' ') # 1 2 3 4 5 6 7 8 9 10
for index, value in enumerate(a):
    print(f"{index}->{value}", end=' ') # 0->1 1->2 2->3 3->4 4->5 5->6 6->7 7->8 8->9 9->10

# dictionary
b = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
for key, value in b.items():
    print(key, value, end=' ') # 1 a 2 b 3 c 4 d 5 e
for key in b.keys():
    print(key, end=' ') # 1 2 3 4 5
for value in b.values():
    print(value, end=' ') # a b c d e
# set
s = {1, 2, 3, 4, 5}
for item in s:
    print(item, end=' ') # 1 2 3 4 5 (order is not guaranteed in sets)
# zip
b = [1, 2, 3, 4, 5]
for item in zip(a, b):
    print(item, end=' ') # (1, 2) (2, 3) (3, 4) (4, 5) (5, 6) (6, 7) (7, 8) (8, 9) (9, 10)
print()

# 3. LIST PROCESSING
print('-'*30, 'LIST PROCESSING', '-'*30)

# push/pop
a = [1, 2, 3]
left = a.pop(0) # 1 # pop from the left (first element) 
right = a.pop() # 3 # pop from the right (last element)
a.append(4) # [2, 4]
a.insert(0,-1) # list.insert(index, value)
print(a) # [-1, 2, 4]

# accumulate (prefix sum)
from itertools import accumulate
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(accumulate(a))) # [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]

# count
from collections import Counter
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count = Counter(a) # Counter({1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1})
count_dict = dict(count) # {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1}

# functional programming (map (built-in), filter (built-in), reduce (functools))
# map
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def squared(x: int) -> int:
  return x * x
print(list(map(squared, a))) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# filter
def is_even(x: int) -> bool:
  return x % 2 == 0
print(list(filter(is_even, a))) # [2, 4, 6, 8, 10]

# reduce
from functools import reduce
def product(acc: int, item: int) -> int:
  return acc * item
print(reduce(product, a)) # 3628800 (1*2*3*4*5*6*7*8*9*10)
print(reduce(lambda acc, item: acc + item, a)) # 55 (1+2+3+4+5+6+7+8+9+10)

# comprehensions
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a_squared = [x * x for x in a] # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
a_filtered = [x for x in a if x % 2 == 0] # [2, 4, 6, 8, 10]

# sort
a = ['abc', 'abd', 'aaa', 'bcd', 'bad', 'bbb']
a.sort()                                       # ['aaa', 'abc', 'abd', 'bad', 'bbb', 'bcd']
a.sort(reverse=True)                           # ['bcd', 'bbb', 'bad', 'abd', 'abc', 'aaa']
a.sort(key=lambda word: word[1], reverse=True) # ['bcd', 'bad', 'bbb', 'abc', 'abd', 'aaa']
b = sorted(a, key=lambda word: word[2])        # ['abc', 'aaa', 'abd', 'bad', 'bbb', 'bcd']


print('-'*30, 'CONDITIONS', '-'*30)
# 4. CONDITIONS
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def is_even(x: int) -> bool:
  return x % 2 == 0
def is_odd(x: int) -> bool:
  return x % 2 == 1
print('All even:', all(is_even(x) for x in a)) # False
print('Any even:', any(is_even(x) for x in a)) # True
print('All odd:', all(list(map(is_odd, a)))) # False
print('Any odd:', any(list(map(is_odd, a)))) # True


# 5. TUPLES
print('-'*30, 'TUPLES', '-'*30)
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20) # Point(x=10, y=20)
# list of tuples
points = [Point(1, 2), Point(0, 4), Point(5, 6)] # [Point(x=1, y=2), Point(x=0, y=4), Point(x=5, y=6)]
# unpacking
x, y = p # 10 20
# sorting tuples (by distance from origin (0, 0))
points.sort(key=lambda point: point.x**2 + point.y**2) # [Point(x=0, y=4), Point(x=1, y=2), Point(x=5, y=6)]
# min/max
print(min(points, key=lambda p: p.x)) # Point(x=0, y=4)
print(max(points, key=lambda p: -p.y)) # Point(x=1, y=2)

# sort (with lambda function)
c = [(10, 'a'), (4, 'b'), (3, 'c'), (2, 'd')]
print(c) # [(10, 'a'), (4, 'b'), (3, 'c'), (2, 'd')]
c.sort(key=lambda p: p[0])
print(c) # [(2, 'd'), (3, 'c'), (4, 'b'), (10, 'a')]

# 6. HEAP
print('-'*30, 'HEAP', '-'*30)
import heapq # heapq is a min-heap by default (minimum element at the top)
heap = [5, 7, 9, 1, 3]
heapq.heapify(heap) # [1, 3, 9, 7, 5]
heapq.heappush(heap, 2) # [1, 2, 9, 7, 5, 3]
print(heapq.heappop(heap)) # 1
print(heap) # [2, 3, 9, 7, 5]
print(heapq.nlargest(3, heap)) # [9, 7, 5]
print(heapq.nsmallest(3, heap)) # [2, 3, 5]