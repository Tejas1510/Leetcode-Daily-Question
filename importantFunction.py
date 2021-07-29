# Find closest number to an entered number in the list
def closest(lst, K): 
      return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))] 

# Find gcd of two entered number
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b) 

# Find LCM of two number
def lcm(a,b):
    return(a*b)//gcd(a,b)    

# Find Sum of Digits
def sumOfDigits(n):
    n=str(n)
    a=list(n)
    a=[int(i) for i in a ]
    sum1=sum(a)
    return sum1
    
# Function to find whether entred number is prime or not
def prime(n): 
      
    if (n == 1): 
        return False
  
    for i in range(2, n + 1): 
        if i * i > n: 
            break
        if (n % i == 0): 
            return False
  
    return True

#Convert a Decimal number(5) to Binary(101)
def decimalToBinary(n): 
    return bin(n).replace("0b","") 

#Convert a Binary Number(101) to Decimal(5)
def binaryToDecimal(n): 
    return int(n,2) 

# Sort a Dictionary in ascending based on its value
import operator
dictionary={1:245,2:456,3:876}
dict1=sorted(dictionary.items(),key=operator.itemgetter(1))

#Sort a Dictionary in descending order based on ots value
import operator
dictionary={1:245,2:456,3:876}
dict2 = dict(sorted(dictionary.items(),key=operator.itemgetter(1),reverse=True))

#Generate all number having odd factor in range(1,1000)
a=[]
for i in range(1,1001):
    a.append(i*i)

#Program to check if a triangle with Positive area is possible
a=list(map(int,input().split()))
a.sort()
for i in range(1,len(a)-1):
    if(a[i-1]+a[i]>a[i+1]):
        print("YES")
        exit()
print("NO")

# Declaration of a linked list in python
class LLNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

# Find the frequency of element in an array
from collections import Counter
nums=[1,1,1,7,2,1]
n=1 #We can enter any thing here
Counter(nums).most_common(n)[0][1] if nums else 0
# This will return the most common element
# [[1,4]]

#Program to find if a target value exist in a binary tree

class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def solve(self, root, target):
        flag=0
        if(target==0):
             return False
        b=bin(target)[3:]
        
        for i in b:
            if(not root):
                return False
            if(i=="1"):
                root=root.right
            else:
                root=root.left
        return(root != None)
        
        
# Reduce Function in python to find gcd of an array
reduce("function_name", "array")
from functools import reduce
from math import gcd
a=[1,2,3,4,56,6]
ans=reduce(gcd,a)

# Longest Common Prefix
#words = ["anthony", "ant", "antigravity"]
#ans = "ant"
def solve(words):
    minword = min(words, key=len,default="")
    for i in range(len(minword),-1,-1):
        if(all(word.startswith(minword[:i]) for word in words )):
                return minword[:i]
    return ""

# integer to base 3
def solve(self, n):
        r = ""
        while n >= 3:
            r = str(n % 3) + r
            n = n // 3
        r = str(n) + r
        return r

# defaultdict
# it takes only one argument what should be the default type
# for example
from collections import defaultdict
dict1 = defaultdict(int)
dict2 = defaultdict(list)

#Making a dictionary of array
a=[1,2,3,2,2,1,3]
for i in range(len(a)):
    dict1[a[i]]=dict1[a[i]]+[i]
print(dict1)
#{1: [0, 5], 2: [1, 3, 4], 3: [2, 6]}

#Index with Equal Left and Right Sums
class Solution:
    def solve(self, x):
        a=0
        s=sum(x)
        for i in range(len(x)):
            if a==s-a-x[i]:return i
            a+=x[i]
        return -1

# Making a dictinary of all alphabets
import string
d = dict.fromkeys(string.ascii_lowercase, 0)
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

# converting list into tuple
a=[1,2,3]
tuple1 = tuple(a)
print(tuple1)
# (1,2,3)

# Dictionary can be used with tuple but not with list
dict1={}
list1=[1,2,3]
tuple1 = tuple(a)
dict1[list1]=1 # not allowed unhashable type error
dict1[tuple1]=1 # allowed

# Finding sum of all elements of a particular row and coulomn in a matrix
matrix = [
    [0, 0, 1],
    [1, 0, 0],
    [0, 1, 0]
]
row = [sum(r) for r in matrix]
col = [sum(c) for c in zip(*matrix)]

# Find the missing term of an aritmetic progression
class Solution:
    def solve(self, nums):
        return (nums[0] + nums[-1]) * (len(nums) + 1) // 2 - sum(nums)

# Get all substrings of string
# Using list comprehension + string slicing
res = [test_str[i: j] for i in range(len(test_str))
          for j in range(i + 1, len(test_str) + 1)]

# how to keep on taking inputs if we don't know n till end of file
while True:
    try:
        n=input()
        # take input and write the entire logic here
    except EOFError:
        #print or return somethin
        break

# enumerate in python
s="ababcbacadefegdehijhklij"
s1=enumerate(s)
# It simply create a object having index and character
#output
# 0 a
# 1 b
# 2 a
# 3 b
# 4 c
# 5 b
# 6 a
# 7 c
# 8 a
# 9 d
# 10 e
# 11 f
# 12 e
# 13 g
# 14 d
# 15 e
# 16 h
# 17 i
# 18 j
# 19 h
# 20 k
# 21 l
# 22 i
# 23 j

# Very Important Merge Interval Function
def merge(a):
        a=sorted(a,key=lambda x:x[0])
        l=a[0][0]
        r=a[0][1]
        b=[]
        
        for i in range(1,len(a)):
            if(a[i][0]<=r and a[i][1]>=l):
                r=max(r,a[i][1])
                l=min(l,a[i][0])
            else:
                b.append([l,r])
                l=a[i][0]
                r=a[i][1]
        b.append([l,r])
        return b
            
# Count all the perfect sqaure below a specified number
n=10
import math
print(int(math.sqrt(n)))

# Find Intersection of n array
n,m=map(int,input().split())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))

# Method 1
ans = list(set.intersection(*[set(x) for x in a]))
ans.sort()
if(len(ans)==0):
    print(-1)
else:
    for i in ans:
        print(i,end=" ")

# Method 2
t1=set(a[0])
for i in range(1,len(a)):
    t1=t1 & set(a[i])
if(t1==set()):
    print(-1)
else:
    print(t1)
