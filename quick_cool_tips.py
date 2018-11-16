# way to format result
>>> format(log_num, '.100f') #with comma
>>> print("%.4f" %a) #without comma

#nice way to get input from user
a0,a1,a2 = input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]

#way to join indivdual variables in one line
result = solve(a0, a1, a2, b0, b1, b2)
print (" ".join(map(str, result)))
#but same as
print(12,34)
a = 12
b = 34
print(a, b)

#cheast way to save lines
a = b = 0

#nice way to loop
for i, j in ((12,34), (34, 56),(76,78)):
	print(i, j)

#comprehensive list (if & else)
>>> l = [22, 13, 45, 50, 98, 69, 43, 44, 1]
>>> print([])
[]
# [false,true][condition]iterate
>>> print([[x+5,x+1][x >= 45] for x in l])
[27, 18, 46, 51, 99, 70, 48, 49, 6]
# [true condition false/else-> do sonthing iterate]
>>> [x+1 if x >= 45 else x+5 for x in l]
[27, 18, 46, 51, 99, 70, 48, 49, 6]

#comaring the triplets hackersrank
#best and most simple
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
print(sum(a > b for a, b in zip(A, B)), sum(a < b for a, b in zip(A, B)))

#trick [concept: true = 1 and false = 0]
>>> res = (4>1) + (34<22) + (9<10)
>>> res
2

#simplest way to sum no loop at all 
# Map all elements in list
print(sum(map(int, input().split())))
# interpretor 
>>> arr
['1', '2', '3', '3', '5', '6']
>>> sum(arr)
'''
Traceback (most recent call last):
  File "<pyshell#202>", line 1, in <module>
    sum(arr)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
'''
>>> sum(list(map(int, arr)))
20


# list constructor
a = list() # is same as a = []

#some smart way of input a array of numbers
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()

#finding & counting digits as a divisor 
#coolest ans 
def func(A):
    return len([1 for i in str(A) if i !='0' and A%int(i)==0])

for t in range(int(input())):
    print(func(int(input())))

#how can the chocolate wrapper problem be so simple 
import sys
if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        N, C, M = list(int(x) for x in sys.stdin.readline().split())
        
        total = N // C
        wrappers = total
        
        while wrappers >= M:
            wrappers += 1 - M
            total += 1
        
        print(total)

# Remember to traverse the 1D-array from right to left
#WRONG METHOD
>>> for i in range(len(ar),0,-1):
...     print(ar[i])

IndexError: list index out of range
#because
for i in range(len(ar),0,-1):
...     print(i)
...
6
5
4
3
2
1
#CORRECT METHOD
>>> ar = [1,3,5,8,9,3]
>>> for i in range(len(ar)-1,-1,-1):
...     print(ar[i])
...
3
9
8
5
3
1

## if you want to start looping from the '1' index not '0'
for i in ar[1:]:
	print(i)

## to round rumbers
>>> a = 234.5655
>>> int(round(a,0))

## To round to next multiple of '5'
>>> er = 67
>>> er + (5-er) % 5

## solution are very simple yet you arnt able to get it
# memory error distraction
print(s.count('a') * (n//L) + s[:n % L].count('a'))

##floor division
>>> 14//5
2
>>> 14/5
2.8

##rotating an array
last = len(a) - d # d= number of elements from left
return (a[-last:] + a[:d])

	#OR
pivot_elem_pos = arr.index(pivot_elem)
return (arr[pivot_elem_pos:] + arr[:pivot_elem_pos])

# Python | Largest, Smallest, Second Largest, Second Smallest in a List
def find_len(list1): 
    length = len(list1) 
    list1.sort() 
    print("Largest element is:", list1[length-1]) 
    print("Smallest element is:", list1[0]) 
    print("Second Largest element is:", list1[length-2]) 
    print("Second Smallest element is:", list1[1]) 
  
# Driver Code 
list1=[12, 45, 2, 41, 31, 10, 8, 6, 4] 
Largest = find_len(list1) 

# reverse a string
a ="GeeksForGeeks"
print("Reverse is", a[::-1]) 

# Reverse A List Using Slicing.
[1, 3, 5][::-1]

# Reverse The List Itself.
testList = [1, 3, 5]
testList.reverse()
print(testList)

# Create a single string from all the elements in list
a = ["Geeks", "For", "Geeks"] 
print(" ".join(a)) 

# Return Multiple Values From Functions.
def x(): 
    return 1, 2, 3, 4
a, b, c, d = x() 
  
print(a, b, c, d)

# Find The Most Frequent Value In A List.
test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4] 
print(max(set(test), key = test.count)) 

# Airthmatic on string and lists
n = 2; 
a ="GeeksforGeeks"; 
print(a * n); 

# initilising array
L= [0] * 10

# ternary operator
[on_true] if [expression] else [on_false]
x = 10 if (y == 9) else 20

def small(a, b, c):
    return a if a <= b and a <= c else (b if b <= a and b <= c else c)

# Work With Multi-Line Strings.
multiStr = "select * from multi_row \
where row_id < 5"
print(multiStr)
#OUTPUT:- select * from multi_row \ where row_id < 5

# One more trick is to use the triple-quotes.

multiStr = """select * from multi_row 
where row_id < 5"""
print(multiStr)
#OUTPUT:- select * from multi_row \n where row_id < 5

# In the Python console, whenever we test an expression or call a function, the result dispatches to a temporary name, _ (an underscore).
>>> 2 + 1
3
>>> _
3
>>> print _
3

# Dict & sets very important
testDict = {i: i * i for i in xrange(10)} 
testSet = {i * 2 for i in xrange(10)}

print(testSet)
#set([0, 2, 4, 6, 8, 10, 12, 14, 16, 18])

print(testDict)
#{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# Unpack Function Arguments Using Splat Operator: an artistic way to unpack arguments lists.
def test(x, y, z):
    print(x, y, z)

testDict = {'x': 1, 'y': 2, 'z': 3} 
testList = [10, 20, 30]

test(*testDict)
test(**testDict)
test(*testList)

#1-> x y z
#2-> 1 2 3
#3-> 10 20 30
print(*testDict)
# x y z

# Awesome way to make a dict of Switch case pair: Must remember
stdcalc = {
    'sum': lambda x, y: x + y,
    'subtract': lambda x, y: x - y
}

print(stdcalc['sum'](9,3))
print(stdcalc['subtract'](9,3))

#1-> 12
#2-> 6

# Create A Dictionary From Two Related Sequences.
t1 = (1, 2, 3)
t2 = (10, 20, 30)

print(dict (zip(t1,t2)))

#-> {1: 10, 2: 20, 3: 30}

# every Python variable is a pointer to the data stored somewhere in memory
# get memory location of a variable using id() function
print(id(age))
59624096

# Order of Operations
#   1. ( )
#   2. **
#   3. * / // %
#   4. + -
#   Example: 1 + 5 ** (3 // 2) - 6 % 4 => 4
x = 1 + 5 ** (3 // 2) - 6 % 4
print(x)

# Strings and cases
s = 'Howdy dude!'
print(s.lower())
print(s.upper()[:5])
print(s.title())
print(s.replace('Howdy', 'Greetings'))
print(s)
print(s.count('d'))
print(s.find('w'))
print('dud' in s)
print('X' not in s)
print(s.startswith('How'))
print(s.endswith('cat'))
print(s > 'Honk')
print(s.isalpha())
print(s[0:4].isalpha())
print(s.isnumeric())
print('73.294'.split('.'))

# Slicing -- slice out substrings, sublists, subtuples using indexes
# [start : end+1 : step]
x = 'computer'
print(x[1:4])           # items 1 to 3, 'omp'
print(x[1:6:2])         # items 1, 3, 5, 'opt'
print(x[3:])            # items 3 to end, 'puter'
print(x[:5])            # items 0 to 4, 'compu'
print(x[-1])            # last item, 'r'
print(x[-3:])           # last 3 items, 'ter'
print(x[:-2])           # all except last 2 items, 'comput'


# Minimum -- find the minimum item in a sequence lexicographically
# alpha or numeric types, but cannot mix types
x = 'bug'
print (min(x))          # prints 'b' 

x = ['pig', 'cow', 'horse']
print (min(x))  

# Sorting -- returns a new list of items in sorted order
# sorted does not change the original list
x = 'bug'
print (sorted(x))       # prints ['b', 'g', 'u']

# x.sort() puts the items of x in sorted order (sorts in place).
x = [5, 3, 8, 6]
x.sort()                # [3, 5, 6, 8]

x = ['pig', 'cow', 'horse']
print (sorted(x))       # prints ['cow', 'horse', 'pig']

# # Append -- append an item to a list
x = [5, 3, 8, 6]
x.append(7)             # [5, 3, 8, 6, 7]

# Extend -- append an sequence to a list
x = [5, 3, 8, 6]
y = [12, 13]
x.extend(y)             # [5, 3, 8, 6, 7, 12, 13]

# Pop -- pops last item off the list, and returns item
x = [5, 3, 8, 6]
x.pop()                 # [5, 3, 8]. and returns the 6
print(x.pop())          # [5, 3]. and prints 8 

# Remove -- remove first instance of an item
x = [5, 3, 8, 6, 3]
x.remove(3)             # [5, 8, 6, 3]


# Tuples are Immutable, but member objects may be mutable
x = (1, 2, 3)
del(x[1])               # error!
x[1] = 8                # error!

x = ([1,2], 3)          # 2-item tuple: list and int
del(x[0][1])            # ([1], 3)

# SETS
# ------------------------------------------------
# constructors – creating a new set
x = {3,5,3,5}           # {5, 3}
x = set()               # empty set
list1 = [5, 7, 7]
x = set(list1)          # new set from list. strips duplicates, {5, 7}

# Set Comprehension
x = {3*x for x in range(10) if x>5} 
# resulting set: {18, 21, 24, 27} but in random order

# DICTIONARIES
# ------------------------------------------------
# constructors – creating a new dict
x = {'pork':25.3, 'beef':33.8, 'chicken':22.7}
x = dict([('pork', 25.3),('beef', 33.8),('chicken', 22.7)])
x = dict(pork=25.3, beef=33.8, chicken=22.7)

# Accessing keys and values in a dict
x.keys()                # returns list of keys in x
x.values()              # returns list of values in x
x.items()               # returns list of key-value tuple pairs in x

item in x.values()      # tests membership in x, returns boolean


