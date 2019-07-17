# Data Structures Implementation

#Array
from array import *

arr = array('i', [5, 9, -2, 1, 0])

char_arr = array('u', ['a', 'e', 'i'])

squared_arr = array(arr.typecode, (a*a for a in arr))

user_arr = array('i', [])

print('\nPrinting a python array of numbers, then another array of characters')

for i in range(len(arr)):
    print(arr[i])

for e in char_arr:
    print(e)


print('\nUsing computation to print squares of number array in one line')
s = 0

while s < len(squared_arr):
    print(squared_arr[s])
    s += 1
#
#n = int(input('Enter the length of the array '))
#
#for u in range(n):
#    index = int(input('Enter the next value '))
#    user_arr.append(index)
#
#print(user_arr)
#
#search_index = int(input('Enter the array value you are searching for to get its index '))
#
#k = 0
#
#for x in user_arr:
#    if x == search_index:
#        print(k)
#        break
#    k += 1
#
#
#List
ex_list = [1, 2, 3.14, 'a', ['b', 'c']]
print('\nExample of a list in python \n' + str(ex_list))

#Tuple
tuple1 = (1, -2)
tuple2 = ('Adrian', '999-999-9999', 'example@email.com')
print('\nExample of tuples\n' + str(tuple1) + '\n' + str(tuple2))

#Set
x = {m for m in range(8)}

print()

print('\nThis is a set.  Sets are unordered and contain unique elements\n' + str(x))

print()

#Dictionary
dictionary1 = {'pork': 22.50, 'beef': 31.25, 'chicken': 18.75}
print('\nLike sets, dictionaries are unordered but instead, contain unique key-value pairs\n' + str(dictionary1))

#Linear Data Structures: List/Array, Linked List, Stack, Queue

#Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None #Make None default value for head

def count_nodes(head):
    count = 1
    current = head
    
    while current.next is not None:
        current = current.next
        count += 1
    return count

class linked_list:
    def __init__(self):
        self.head = None
        
    def reverse_iterative(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    
    def show_nodes(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
llist = linked_list()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
llist.push(5)
llist.push(6)

print(f'\nThis linked list has {count_nodes(llist.head)} nodes\n')

llist.show_nodes()

print('\nThis list has been reversed iteratively')       
llist.reverse_iterative()
print()
llist.show_nodes()

#Stack

#implemented as a class
print('\nStack')
class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def get_stack(self):
        return self.items

    def is_empty(self):
        return self.items==[]

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.get_stack())
s.push(4)
print(s.get_stack())
s.pop()
print(s.get_stack())
print(str(s.is_empty()) + ' <-- Is the stack empty?')
s.pop()
s.pop()
s.pop()
print(str(s.get_stack()) + ' <-- An empty stack')
print(str(s.is_empty()) + ' <-- Now the stack is empty')
s.push('A')
print(str(s.peek()) + ' <-- After adding an "A" peeks at the top of stack') 
print()

#Queue
from collections import deque
print('Queue')
class Queue():
    def __init__(self):
        self.items = deque()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def pop_left(self):
        self.items.popleft()

    def get_queue(self):
        return self.items

q = Queue()
q.push('A')
q.push('B')
q.push('C')
print(q.get_queue())
q.pop_left()
print(q.get_queue())
q.pop()
print(q.get_queue())

print()


#Binary Search Tree - used to store naturally hierarchial data like a file system. EX. Network routing algorithms
#Node values are ordered, beginning after the root,  with the left child less than the parent and the right child greater than
#The leftmost node should be the smallest, the root in the middle, and the rightmost the greatest
#Olog(n) time complexity
print('BST')
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
    #add node
    def add(self, val):
        if(self.root == None):
            self.root = Node(val)
        else:
            self.add_node(self.root, val)

    #node should not be null
    def add_node(self, node, val):
        if(node.val < val):
            self.add_right(node, val)
        else:
            self.add_left(node, val)

    def add_right(self, node, val):
        if(node.right == None):
            node.right = Node(val)
        else:
            self.add_node(node.right, val)

    def add_left(self, node, val):
        if(node.left == None):
            node.left = Node(val)
        else:
            self.add_node(node.left, val)

    def printTree(self):
        if(self.root != None):
            self._printLabel(self.root)
            self._printTree(self.root)

    def _printLabel(self, node):
        if(node != None):
            print('Node ' + str(node.val))
            self._printLabel(node.left)
            self._printLabel(node.right)

    def _printTree(self, node):
        if(node != None):
            if(node.left != None):
                print('Node ' + str(node.val) + '\'s left child is ' + str(node.left.val)) 
            if(node.right != None):
                print('Node ' + str(node.val) + '\'s right child is ' + str(node.right.val)) 

            self._printTree(node.left)
            self._printTree(node.right)
            
tree = Tree()
tree.add(5)
tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(1)
tree.add(2)
tree.add(7)
tree.add(9)
tree.printTree()
print()
#Heap - Min/Max heaps have their min/max node at the root of a binary tree
#parent nodes are always less than their children for a min heap and greater than for a max heap
#it is complete and not unbalanced
#heaps are one maximally efficient implementation of a priority queue data type
#it has nothing to do with the memory pool from which dynamically allocated memory is allocated
#O(1) time complexity

print('Max Heap')

class Heap(object):

    HEAP_SIZE = 10;

    def __init__(self):
        self.heap = [0]*Heap.HEAP_SIZE
        self.currentPosition = -1

    def insert(self, item):
        if(self.isFull()):
            print('Heap is full')
            return
        
        self.currentPosition = self.currentPosition + 1
        self.heap[self.currentPosition] = item
        self.fixUp(self.currentPosition)

    def fixUp(self, index):
        parentIndex = int((index - 1)/2)

        while(parentIndex >= 0 and self.heap[parentIndex] < self.heap[index]):
            temp = self.heap[index]
            self.heap[index] = self.heap[parentIndex]
            self.heap[parentIndex] = temp
            index = parentIndex
            parentIndex = int((index - 1)/2)

    def getMax(self):
        result = self.heap[0]
        self.currentPosition = self.currentPosition - 1
        self.heap[0] = self.heap[self.currentPosition]
        del self.heap[self.currentPosition + 1]
        self.fixDown(0, -1)
        return result

    def fixDown(self, index, upto):
        if(upto < 0):
            upto = self.currentPosition

        while(index <= upto):
            leftChild = 2 * index + 1
            rightChild = 2 * index + 2

            if(leftChild <= upto):
                childToSwap = None

                if(rightChild > upto):
                    childToSwap = leftChild
                else:
                    if(self.heap[leftChild] > self.heap[rightChild]):
                        childToSwap = leftChild
                    else:
                        childToSwap = rightChild

                if(self.heap[index] < self.heap[childToSwap]):
                    temp = self.heap[index]
                    self.heap[index] = self.heap[childToSwap]
                    self.heap[childToSwap] = temp
                else:
                    break

                index = childToSwap

            else:
                break
    
    #perform O(N logN) sorting IN PLACE
    def heapsort(self):
        for i in range(0,self.currentPosition + 1):
            temp = self.heap[0]
            print("%d " % temp)
            self.heap[0] = self.heap[self.currentPosition - i]
            self.heap[self.currentPosition - i] = temp
            self.fixDown(0, self.currentPosition - i - 1)


    def isFull(self):
        if(self.currentPosition == Heap.HEAP_SIZE):
            return True
        else:
            return False

heap = Heap()
heap.insert(12)
heap.insert(-3)
heap.insert(23)
heap.insert(4)
heap.heapsort()

print()
#Hashmap
print('Hashmap')







print()
#Graph
class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}  #key is vertex obj, value is cost

    def addNeighbor(self, nbr, cost = None): #nbr is vertex obj
        self.connectedTo[nbr] = cost

    #printing
    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):   #returns vertex objects list
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):  #nbr vertex object
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}  #dict of id key and vertex obj value
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n): #returns Vertex object with id n
        if(n in self.vertList):
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n): #check if vertex object n in self
        return n in self.vertList


    #graph user will need to call this twice for undirected graph
    def addEdge(self, f, t, cost = 0): #note nv not used
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self): #gets list of ids, not vertex objects
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


print()
print('A Simple graph')
#create a simple graph without direction
def add_both_edges(g, key1, key2):
    g.addEdge(key1, key2)
    g.addEdge(key2, key1)

g = Graph()
add_both_edges(g, 'Mary', 'Sam')
add_both_edges(g, 'Mary', 'Tom')
add_both_edges(g, 'Mary', 'Joe')
add_both_edges(g, 'Joe', 'Tom')
g.addVertex('Sally')

#printing
for from_id in g.getVertices():
    t = tuple(v.id for v in g.getVertex(from_id).connectedTo.keys())
    print(f'edge: {from_id} to {t}')

print()

#create a directed graph
print('Directed graph')
h = Graph()
h.addEdge('V0', 'V1', 5)
h.addEdge('V0', 'V5', 2)
h.addEdge('V1', 'V2', 4)
h.addEdge('V2', 'V3', 9)
h.addEdge('V3', 'V4', 7)
h.addEdge('V3', 'V5', 3)
h.addEdge('V4', 'V0', 1)
h.addEdge('V5', 'V2', 1)
h.addEdge('V5', 'V4', 8)


#printing
for from_id in h.getVertices():
    t = tuple(f'{v.id}:{cost}' for v, cost in h.getVertex(from_id).connectedTo.items())
    print(f'edge: {from_id} to : {t}')



print()





#Matrix
print('Matrix math')
from numpy import *


arr1 = array([
    [1, 2, 3],
    [4, 5, 6]
])

arr2 = arr1.flatten()

arr3 = arr2.reshape(3, 2)

print(arr1)

print()

print(str(arr2) + ' flattened')

print()

print(str(arr3) + ' reshaped\n') 

m = matrix('1 2 3; 4 5 6')
n = matrix('1 2 3; 3 4 42')
o = matrix('1 0; 0 1; 0 0')

print(m)
print()
print(n)
print()
print(o)

print()

print(str(m) + ' matrix m')

print()

print(str(m + n) + 'matrix n')

print()

#[1*1+2*0+3*0= 1 1*0+2*1+3*0= 2]    Each index in [1stRow*1stCol 1stRow*2ndCol]
#[3*1+4*0+42*0= 3 3*0+4*1+42*0= 4]                [2ndRow*1stCol 2ndRow*2ndCol]
print(str(n * o) + ' matrix n * matix o\n')
print('''[1*1+2*0+3*0= 1 1*0+2*1+3*0= 2]    Each index in [1stRow*1stCol 1stRow*2ndCol]
[3*1+4*0+42*0= 3 3*0+4*1+42*0= 4]                [2ndRow*1stCol 2ndRow*2ndCol]
''')




