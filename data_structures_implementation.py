# Data Structures Implementation

#Array
from array import *

arr = array('i', [5, 9, -2, 1, 0])

char_arr = array('u', ['a', 'e', 'i'])

squared_arr = array(arr.typecode, (a*a for a in arr))

user_arr = array('i', [])

for i in range(len(arr)):
    print(arr[i])

for e in char_arr:
    print(e)

s = 0

while s < len(squared_arr):
    print(squared_arr[s])
    s += 1

n = int(input('Enter the length of the array '))

for u in range(n):
    index = int(input('Enter the next value '))
    user_arr.append(index)

print(user_arr)

search_index = int(input('Enter the array value you are searching for to get its index '))

k = 0

for x in user_arr:
    if x == search_index:
        print(k)
        break
    k += 1


#List


#Tuple


#Set


#Dictionary


#Linked List


#Stack


#Queue


#Tree


#Binary Search Tree


#Heap


#Hashing/Hashmap/Hashtable


#Graph


#Matrix
from numpy import *


arr1 = array([
    [1, 2, 3],
    [4, 5, 6]
])

arr2 = arr1.flatten()

arr3 = arr2.reshape(3, 2)

print(arr1)

print()

print(arr2)

print()

print(arr3)

m = matrix('1 2 3; 4 5 6')
n = matrix('1 2 3; 3 4 42')
o = matrix('1 0; 0 1; 0 0')

print()

print(m)

print()

print(m + n)

print()

#[1*1+2*0+3*0= 1 1*0+2*1+3*0= 2]    Each index in [1stRow*1stCol 1stRow*2ndCol]
#[3*1+4*0+42*0= 3 3*0+4*1+42*0= 4]                [2ndRow*1stCol 2ndRow*2ndCol]
print(n * o)