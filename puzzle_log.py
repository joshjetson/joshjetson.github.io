#This file is a log of some completed leet code puzzles.

# Python3 program to find the maximum depth of tree

# A binary tree node
puzzles = 'https://www.w3resource.com/python-exercises/lambda/index.php'
class Node:

	# Constructor to create a new node
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

# Compute the "maxDepth" of a tree -- the number of nodes
# along the longest path from the root node down to the
# farthest leaf node
def maxDepth(node):
	if node is None:
		return -1 ;

	else :

		# Compute the depth of each subtree
		lDepth = maxDepth(node.left)
		rDepth = maxDepth(node.right)

		# Use the larger one
		if (lDepth > rDepth):
			return lDepth+1
		else:
			return rDepth+1


# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


print ("Height of tree is %d" %(maxDepth(root)))

""" 
    Author   : Ajinkya Sonawane
"""
class Node:
    def __init__(self,data,level,fval):
        """ Initialize the node with the data, level of the node and the calculated fvalue """
        self.data = data
        self.level = level
        self.fval = fval
def generate_child(self):
        """ Generate child nodes from the given node by moving the blank space
            either in the four directions {up,down,left,right} """
        x,y = self.find(self.data,'_')
        """ val_list contains position values for moving the blank space in either of
            the 4 directions [up,down,left,right] respectively. """
        val_list = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
        children = []
        for i in val_list:
            child = self.shuffle(self.data,x,y,i[0],i[1])
            if child is not None:
                child_node = Node(child,self.level+1,0)
                children.append(child_node)
        return children
        
    def shuffle(self,puz,x1,y1,x2,y2):
        """ Move the blank space in the given direction and if the position value are out
            of limits the return None """
        if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
            temp_puz = []
            temp_puz = self.copy(puz)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None
def copy(self,root):
        """ Copy function to create a similar matrix of the given node"""
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp    
            
    def find(self,puz,x):
        """ Specifically used to find the position of the blank space """
        for i in range(0,len(self.data)):
            for j in range(0,len(self.data)):
                if puz[i][j] == x:
                    return i,j
class Puzzle:
    def __init__(self,size):
        """ Initialize the puzzle size by the specified size,open and closed lists to empty """
        self.n = size
        self.open = []
        self.closed = []
def accept(self):
        """ Accepts the puzzle from the user """
        puz = []
        for i in range(0,self.n):
            temp = input().split(" ")
            puz.append(temp)
        return puz
def f(self,start,goal):
        """ Heuristic Function to calculate hueristic value f(x) = h(x) + g(x) """
        return self.h(start.data,goal)+start.level
def h(self,start,goal):
        """ Calculates the different between the given puzzles """
        temp = 0
        for i in range(0,self.n):
            for j in range(0,self.n):
                if start[i][j] != goal[i][j] and start[i][j] != '_':
                    temp += 1
        return temp
def process(self):
        """ Accept Start and Goal Puzzle state"""
        print("Enter the start state matrix \n")
        start = self.accept()
        print("Enter the goal state matrix \n")        
        goal = self.accept()
start = Node(start,0,0)
        start.fval = self.f(start,goal)
        """ Put the start node in the open list"""
        self.open.append(start)
        print("\n\n")
        while True:
            cur = self.open[0]
            print("")
            print("  | ")
            print("  | ")
            print(" \\\'/ \n")
            for i in cur.data:
                for j in i:
                    print(j,end=" ")
                print("")
            """ If the difference between current and goal node is 0 we have reached the goal node"""
            if(self.h(cur.data,goal) == 0):
                break
            for i in cur.generate_child():
                i.fval = self.f(i,goal)
                self.open.append(i)
            self.closed.append(cur)
            del self.open[0]
""" sort the opne list based on f value """
            self.open.sort(key = lambda x:x.fval,reverse=False)
puz = Puzzle(3)
puz.process()
###############################################################
#Find the singular item in a list
#The count method will count how many times something is in an array in python.
# Additionally I have chose to sort the list, print out the sorted duplicated items in order
# and print the singular item in the list last.

num_list = [1, 1, 3, 4, 7, 3, 7]
num_list.sort()#Here I use the sort method to sort the list
count = []
singular = 0
check_list = []
for num in num_list:
	count.append(1)
	if len(count) == len(num_list):
		print('The only unique number in the list is: %d' %(singular))
	elif num_list.count(num) < 2:
		singular += num
	elif num_list.count(num) >= 2:
		if num not in check_list:
			check_list.append(num)
			print('The number %d' %(num), 'is a duplicate')
#Quicker way
nums_count = ['singular digit =  {0}'.format(x) for x in num_list if num_list.count(x) == 1]
#Using lambda
result = lambda x: list(filter(lambda y: (x.count(y) == 1), x))
result(num_list)
#Toshiba satellite model pslb8u-02w003 and a compaq presario v3000
#4007 lowell ave, el sereno 90032 apt C
yurys_email = 'yokaighost1982@gmail.com'

#Write a python program to rearrange positive and negative integers in a given array using lambda
nums = [-1, 2, -3, 5, 7, 8, 9, -10]
result = sorted(l1, key = lambda i: 0 if i == 0 else -1 / i)#-1 / i explained:
# using sorted in this way tells sorted to give you the smallest number first starting from 0 and if not just give
#me anything after zero which results in an ascending order. The else condition does something similar for the
#negative numbers. When you evaluate -1 / -i you get a decimal -1/-10 = 0.1, -1/-3 = 0.3, -1/-1 = 1. Thus
#the sort method can understand the sequence its return value should be is from the smallest to largest
#negative integer. This results in hill arrangement pushing the larger values towards the middle. 

#Write a Python program to count the even, odd numbers in a given array of integers using Lambda.
nums = [1, 2, 3, 5, 7, 8, 9, 10]
print("Original arrays:")
print(array_nums)
odd_ctr = len(list(filter(lambda x: (x%2 != 0), nums)))
even_ctr = len(list(filter(lambda x: (x%2 == 0), nums)))
#or combined in a gnarly solution
result = lambda x: ('{0} EVEN NUMBERS'.format(len(list(filter(lambda y: (y%2 == 0),x)))), '{0} ODD NUMBERS'.format(len(list(filter(lambda y: (y%2 == 1),x)))))

#Understanding list comprension with filters
#Lets first look at the syntax
#the_list_comp = [f(x) for x in array if x > 5]
	#What the above is saying is that if x in the array is larger then 5 it will then send that value
	#into the function f()

#Write a Python program to find the values of length six in a given list using Lambda.
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days = filter(lambda day: day if len(day)==6 else '', weekdays)
for d in days:
  print(d)
  #Using list comprehension
  day_lst = [day for day in days if len(day)==6]
  #A more dynamic solution
  result = lambda x, y: list(filter(lambda z: (len(z) == y), x))
  result(weekdays, 6)# = ['Monday', 'Friday', 'Sunday']
# Write a Python program to add two given lists using map and lambda
num1 = [1,2,3]
num2 = [4,5,6]
combine = list(map(lambda a, b: a + b, num1, num2))#This simplifies to
#using list comprehension
combine = [*map(lambda a, b: a + b, num1, num2)]

#Write a program that takes some input of student grades and find the second lowest score out of the
#n number of students.
students = []
sec_name = []
second_low = 0
n = int(input("Input number of students: "))
for _ in range(n):
   s_name = input("Name: ")
   score = float(input("Grade: "))
   students.append([s_name,score])
print("\nNames and Grades of all students:")
print(students)
order =sorted(students, key = lambda x: int(x[1]))
for i in range(n):
   if order[i][1] != order[0][1]:
       second_low = order[i][1]
       break
print("\nSecond lowest grade: ",second_low)
sec_student_name = [x[0] for x in order if x[1] == second_low]
sec_student_name.sort()
print("\nNames:")
for s_name in sec_student_name:
   print(s_name)
   #A more elegant readable error proof solution below:
import os
os.system('clear')
saying = 'Error: Reset ALL: Please enter only letters for name\nand only numbers for score'
none = ''
while True:
    n_amount = input('How many students: ')
    if n_amount.isnumeric():
        break
n = int(n_amount)
students = []
while range(n):
    os.system('clear')
    print(none)
    name = input('{0} Students remaining: Enter student name: '.format(n))
    score = input('Enter a score for {0}: '.format(name))
    if name.isalpha() and score.isnumeric():
        students.append([name.title(),score])
        none = ''
        n -= 1
    else:
        students = []
        none = saying
        n = int(n_amount)
order =sorted(students, key = lambda x: int(x[1]))
for i in range(int(n_amount)):
    if order[i][1] != order[0][1]:
        chosen = order[i]
        break
print('The second lowest score belongs to {0} whose score is {1} '.format(chosen[0], chosen[1]))
#Write a python program using lambda that will find numbers divisible by 19 and 13 from a list.
	#One way using the map function
	nums = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
	divisible = list(map(lambda x: x if x%19 == 0 or x%13 == 0 else '', nums))# Not the best solution but is a solution

	#Solution using the filter function
	divisible = list(filter(lambda x: (x%19 == 0 or x%13 == 0), nums))# A better solution. Cleaner

	#Solution using list comprehension
	divisible = [x for x in nums if x%19 == 0 or x%13 == 0]# Maybe the best solution

#Write a Python program to find palindromes in a given list of strings using Lambda
strings = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
	#using a filter
	palindrome = list(filter(lambda x: (x[0] == x[len[x]-1], strings)))#Kind of gnarly solution but still pretty cool
	#or
	result = list(filter(lambda x: (x == "".join(reversed(x))), texts))# a bit less thinking here easier to read
	#The confusing condition using join? Lets take a look at this josh. So what is happening here is using the join
	# we are taking the string '' whatever it may be and we are reversing it and this essentially creates the filter
	#because we are saying if x is equal to the reverse of x then show us what x is.

	#using list comprehension
	palindrome = [x for x in strings if x[0] == x[len(x)-1]]#Slightly less aracane easily more elegant but still kind of gnarly solution
#The solution to this problem is the following list comprehension.
  palindrome = [x for x in strings if x[::-1] in strings]

  #A more dynamic approach using lambda
  result = lambda x: list(filter(lambda y: (y[::-1] == y), x))
  result(strings)

#Write a Python program to find all anagrams of a string in a given list of strings using
	anagram = ['bcda', 'abce', 'cbda', 'cbea', 'adcb', 'sjdfh']

  result = lambda x: set([''.join(sorted(y)) for y in x])

  #revised for lists
  result = lambda x: [''.join(sorted(t)) for t in x ]
  r2 = [x for x in result(l1) if result(l1).count(x) > 1]



	# function to check if two strings are
	# anagram or not
	def check(s1, s2):
	 
	# the sorted strings are checked
	if(sorted(s1)== sorted(s2)):
	    print("The strings are anagrams.")
	else:
	    print("The strings aren't anagrams.")        
	     
	# driver code 
	s1 ="listen"
	s2 ="silent"
	check(s1, s2)

# Function to return all anagrams together 
def allAnagram(some_list): 
      
    # empty dictionary which holds subsets 
    # of all anagrams together 
    dict = {} 
  
    # traverse list of strings 
    for strVal in some_list: 
          
        # sorted(iterable) method accepts any 
        # iterable and rerturns list of items 
        # in ascending order 
        key = ''.join(sorted(strVal)) 
          
        # now check if key exist in dictionary 
        # or not. If yes then simply append the 
        # strVal into the list of it's corresponding 
        # key. If not then map empty list onto 
        # key and then start appending values 
        if key in dict.keys(): 
            dict[key].append(strVal)
        else: 
            dict[key] = [] 
            dict[key].append(strVal) 
  
    # traverse dictionary and concatenate values 
    # of keys together 
    output = "" 
    for key,value in dict.items(): 
        output = output + ' '.join(value) + ' '
  
    return output

#A simplified way of doing this
anagram = ['bcda', 'abce', 'cbda', 'cbea', 'adcb', 'sjdfh']
anagram_sort = []
es = set()
for x in anagram:
	anagram_sort.append(''.join(sorted(x)))
	if anagram_sort.count(''.join(sorted(x))) > 1:
		es.add(''.join(sorted(x)))
for x in list(es):
	print('An anagram with the characters {0}, appears {1} times in the list'.format(x, anagram_sort.count(x)))
#write python program to find number in string and store number in list which list is smaller than number sort the numbers.
#Write a Python program to find the numbers of a given string and store them in a list, display the numbers 
#which are bigger than the length of the list in sorted form. Use lambda function to solve the problem.
str1 = "sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5"
print("Original string: ",str1)
str_num=[i for i in str1.split(' ')]
lenght=len(str_num)
numbers=sorted([int(x) for x in str_num if x.isdigit()])
print('Numbers in sorted form:')
for i in ((filter(lambda x:x>lenght,numbers))):
    print(i,end=' ')

#A much much more simple and elegant solution
result = lambda x: sorted(list(filter(lambda y: (y.isdigit() and int(y) > len(x)), x)))

#Using the reduce function from the functools module ?? WHy did I put this here?
  from functools import reduce
  reduce(lambda a, b: bool(a) or bool(b), l) 

  fib_series = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],range(n-2), [0, 1])

  #If we want to find the product of a group of iterables. Python doesnt have a built in function or method 
  #for finding the product so we can use the reduce function in a case like this. 
  #The reduce function essentially allows you to input a list into your lambda function. 

  l = [1, 2, 3, 4 ,5, 6]
  reduce(lambda a, b: a * b, l)

#Scopes, Closures and Decorators
  #Some concepts to remember 
  # Global scope variables can be accessed from inner functions and modified using the global keyword
  #In terms for loops we can assign values to variables inside them and those variables are still 
  #accessible outside of the loop as long as we are accessing it in the same scope the loop was created.
  #If we want to modify an outer scope functions variable from an inner function
  #We can tell python that the variable we want to modify is a nonlocal variable by using the keyword
  nonlocal x
  #Some key takeaways:
    #If we have a global variable that is equal to some value and then we create a function and within that
    #function we create a new variable with the same name as a global variable. Python will then interpret the
    #variable inside of the function as a local variable and not associate it with the other variable which has
    #the same name outside of the function at a global level. 
    #This means that inside a function you can create variables with the same name as variables which already
    #exist outside of the newly created function.
    #EX>
  x = 100
  def example(n):
    x = n ** 2
    return x
    #Another example

  x = 1000

  def example2(n):
    x = n**2
    def inner():
      print(x)
    return inner()#Here what happens is inner takes the assignment of x from its outerscope function.
    #EX..
  x = 100
  def example3(n):
    x = n ** 2
    def innerex():
      nonlocal x#This line of code is saying hey I want to modify the outerscope variable x
      #Without the nonlocal keyword x defined here would simply be considered a local variable
      #local to this innerex function.
      x = 'MODIFIED'

    return inner()

#Closures and free variable
#Standard example of cloure.
def outer():
  x = 'python'
  def inner():
    print(x)
  return inner
fn = outer()
#We have now defined fn equal to the closure and we can now call
 #We can now look at things like the free variables
 fn.__code__.co_freevars
 ('x',) #As we see here there is only one free variable in this closure.
 fn.__closure__#We can look at the closure like this

 def outer():
  x = [1, 2, 3]
  print(hex(id(x)))
  def inner():
    x = [1, 2, 3]#Not a free variable it is now in this form a new local variable.
    print(hex(id(x)))
  return inner
#PYNOTES

#Cool little algorithm I made to filter uneeded characters in strings
def interpret(command: str) -> str:
    clean_string = command.replace('()', 'o').replace('(al)', 'al')
    clean_string = filter(lambda x: x.isalnum() or x.isspace(), clean_string)
    clean_string = "".join(clean_string)
    return clean_string
#The random module
import random
import sys


help('random')
WORDS = ("python", "jumble", "easy", "difficult", "answer",  "xylophone", "G()(al)", "J()@s(h)%", "(H)*^ub*^%$r^&^i*@&(s)")
for element in WORDS:
    word = random.choice(WORDS)
    print(word)
#Smart alternative to if statement
def show_info(chosen_item="phone"):
  info_dict = {
    "phone": "Handheld communication device",
    "car": "Self-propelled ground vehicle",
    "dinosaur": "Extinct lizard"
  }
  
  return info_dict.get(chosen_item, "No info available")


def add_one(x):
  return x + 1

def divide_by_two(x):
  return x/2

def square(x):
  return x**2

def invalid_op(x):
  raise Exception("Invalid operation")

# The better way:
def perform_operation(x, chosen_operation="add_one"):
  ops = {
    "add_one": add_one,
    "divide_by_two": divide_by_two,
    "square": square
  }
  
  chosen_operation_function = ops.get(chosen_operation, invalid_op)
  
  return chosen_operation_function(x)

#Some general notes on lambda functions
#Lambda functions can be powerful and used in arrays. The following is an example of this concept.

import datetime
now = datetime.datetime.now()

ll = [lambda x: x.year, lambda x: x.month, lambda x: x.day, lambda x: x.time()]
print(11[1](now))
#can make a quick loop to cycle through all the elements
for x in ll:
  print(x(now))


 #Using the reduce function from the functools module
  from functools import reduce
  reduce(lambda a, b: bool(a) or bool(b), l) 

  fib_series = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],range(n-2), [0, 1])

  #If we want to find the product of a group of iterables. Python doesnt have a built in function or method 
  #for finding the product so we can use the reduce function in a case like this. 
  #The reduce function essentially allows you to input a list into your lambda function. 

  l = [1, 2, 3, 4 ,5, 6]
  reduce(lambda a, b: a * b, l)

#Scopes, Closures and Decorators
  #Some concepts to remember 
  # Global scope variables can be accessed from inner functions and modified using the global keyword
  #In terms for loops we can assign values to variables inside them and those variables are still 
  #accessible outside of the loop as long as we are accessing it in the same scope the loop was created.
  #If we want to modify an outer scope functions variable from an inner function
  #We can tell python that the variable we want to modify is a nonlocal variable by using the keyword
  nonlocal x
  #Some key takeaways:
    #If we have a global variable that is equal to some value and then we create a function and within that
    #function we create a new variable with the same name as a global variable. Python will then interpret the
    #variable inside of the function as a local variable and not associate it with the other variable which has
    #the same name outside of the function at a global level. 
    #This means that inside a function you can create variables with the same name as variables which already
    #exist outside of the newly created function.
    #EX>
  x = 100
  def example(n):
    x = n ** 2
    return x
    #Another example

  x = 1000

  def example2(n):
    x = n**2
    def inner():
      print(x)
    return inner()#Here what happens is inner takes the assignment of x from its outerscope function.
    #EX..
  x = 100
  def example3(n):
    x = n ** 2
    def innerex():
      nonlocal x#This line of code is saying hey I want to modify the outerscope variable x
      #Without the nonlocal keyword x defined here would simply be considered a local variable
      #local to this innerex function.
      x = 'MODIFIED'

    return inner()

#Closures and free variable
#Standard example of cloure.
def outer():
  x = 'python'
  def inner():
    print(x)
  return inner
fn = outer()
#We have now defined fn equal to the closure and we can now call
 #We can now look at things like the free variables
 fn.__code__.co_freevars
 ('x',) #As we see here there is only one free variable in this closure.
 fn.__closure__#We can look at the closure like this

 def outer():
  x = [1, 2, 3]
  print(hex(id(x)))
  def inner():
    x = [1, 2, 3]#Not a free variable it is now in this form a new local variable.
    print(hex(id(x)))
  return inner
#PYNOTES

#Cool little algorithm I made to filter uneeded characters in strings
def interpret(command: str) -> str:
    clean_string = command.replace('()', 'o').replace('(al)', 'al')
    clean_string = filter(lambda x: x.isalnum() or x.isspace(), clean_string)
    clean_string = "".join(clean_string)
    return clean_string
#The random module
import random
import sys


help('random')
WORDS = ("python", "jumble", "easy", "difficult", "answer",  "xylophone", "G()(al)", "J()@s(h)%", "(H)*^ub*^%$r^&^i*@&(s)")
for element in WORDS:
    word = random.choice(WORDS)
    print(word)
#Smart alternative to if statement
def show_info_about_item(chosen_item="phone"):
  info_dict = {
    "phone": "Handheld communication device",
    "car": "Self-propelled ground vehicle",
    "dinosaur": "Extinct lizard"
  }
  
  return info_dict.get(chosen_item, "No info available")


def add_one(x):
  return x + 1

def divide_by_two(x):
  return x/2

def square(x):
  return x**2

def invalid_op(x):
  raise Exception("Invalid operation")

# The better way:
def perform_operation(x, chosen_operation="add_one"):
  ops = {
    "add_one": add_one,
    "divide_by_two": divide_by_two,
    "square": square
  }
  
  chosen_operation_function = ops.get(chosen_operation, invalid_op)
  
  return chosen_operation_function(x)

#Some general notes on lambda functions
#Lambda functions can be powerful and used in arrays. The following is an example of this concept.

import datetime
now = datetime.datetime.now()

ll = [lambda x: x.year, lambda x: x.month, lambda x: x.day, lambda x: x.time()]
print(11[1](now))
#can make a quick loop to cycle through all the elements
for x in ll:
  print(x(now))

#Write a Python program that multiply each number of given list with a given number using lambda function
nums = [2, 4, 6, 9, 11]
num = 2
calc = list(map(lambda x: x * num, nums))
#And using list comprehension
calc = [x * num for x in nums]#Easily the better choice

#Write a Python program that sum the length of the names of a given list of names after removing the names that starts with an 
#lowercase letter. Use lambda function.
names = ['Josh', 'Paulina', 'mildred', 'Andy', 'Rose', 'Emma', 'yusef', 'gordo']
#One way of doing this using list comprehension
fiter_names = [x for x in names if x.istitle()]
#Then obviously just a simple
len(filter_names)
#using lambda and the filter function
filter_names = list(filter(lambda x: (x.istitle()), names))

#Write a Python program to calculate the sum of the positive and negative numbers of a given list of numbers using lambda function
l = [2, 4, -6, -9, 11, -12, 14, -5, 17]
total_negative_nums = list(filter(lambda nums:nums<0,nums))
total_positive_nums = list(filter(lambda nums:nums>0,nums))
#or you could
nums = list(filter(lambda nums:nums<0,nums)), list(filter(lambda nums:nums>0,nums))
#using list comprension
nums = sum([x for x in l if x>=0]), sum([x for x in l if x<0])#Creating a tuple
#Write a Python program to find numbers within a given range where every number is divisible by every digit it contains
rng = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
#possibly use divmod
#The any() function returns True if any element of an iterable is True. If not, it returns False
def divisible_by_digits(start_num, end_num):
    return [n for n in range(start_num, end_num+1) \
                if not any(map(lambda x: int(x) == 0 or n%int(x) != 0, str(n)))]
print(divisible_by_digits(1,22))

counter = 0
rng = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
digit = rng[counter]
def dbd(nums, num):
  n = num
  emp = []
  for x in nums:
    z, m = divmod(n, x)
    if counter > len(rng):
      break
    if not m:
      emp.append(n)
      counter += 1
      dbd(rng, digit)

def dbd(nums):
  counter = 0
  digit = nums[counter]
  emp = []
  for x in nums:
    z, m = divmod(digit, x)
    if counter > len(nums) - 1:
      break
    if not m:
      emp.append(digit)
  counter += 1
  if counter < len(nums) - 1:
    dbd(rng)
  return emp

counter = 0
def dbd(nums, count):
  global counter
  digit = nums[count]
  emp = []
  m = 0
  for x in nums:
    m = x / digit
    if count > len(nums) - 2:
      break
    if not m:
      emp.append(digit)
  if count <= len(nums) - 2:
    counter += 1
    dbd(rng, counter)
  return emp
counter = 0
emp = []
def dbd(nums, count):
  global counter
  global emp
  digit = nums[count]
  m = 0
  for x in nums:
    z, m = divmod(x, digit)
    if count > len(nums) - 1:
      break
    if not m:
      emp.append(x)
  if count <= len(nums) - 2:
    counter += 1
    dbd(rng, counter)
  return emp

#Write a Python program to create the next bigger number by rearranging the digits of a given number.
#12 turns into 21 or 120 turns into 210

number = 234
def maxit(num):
  num_to_str = str(num)
  max_of = max(num_to_str)



#Write a Python program to find the list with maximum and minimum length using lambda.
	len_list = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
	#Without using lambda
	max_min = [len(max(len_list)), max(len_list)], [len(min(len_list)), min(len_list)]
	#using lambda, if you must..
	lam_max = [lambda x: len(max(x)), lambda x: max(x)]
	lam_min = [lambda x: len(min(x)), lambda x: min(x)]
	#Then these lambda functions can be called in the following way, ex.
	lam_max[0](len_list), lam_max[1](len_list)
	lam_min[0](len_list), lam_min[1](len_list)
#Write a Python program to sort each sublist of strings in a given list of lists using lambda.
	list_ = [['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]
	#Solution using lambda
	clean = lambda x: sorted(x, reverse=True)
	#Then
	print(clean(list_))

#Write a Python program to sort a given list of lists by length and value using lambda.
	val_len = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
	#Nice solution using lambda
	result = lambda x:sorted(x, key=lambda l: (len(l), l))
	result(val_len)
#Write a Python program to find the maximum value in a given heterogeneous list using lambda
hetero = ['Python', 3, 2, 4, 5, 'version']
#solution using lambda
max(hetero, key= lambda x: (isinstance(x, int), x))#Not sure why this concept does not work for min

#Write a program which organizes student grades stored in a tuple from lowest to highest using lambda.
#solution
tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
print(tuple(sorted(list(tuple1), key=lambda x: x[1])))

#Write a Python program to sort a given matrix in ascending order according to the sum of its rows using lambda.
m1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
m2 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
#solution
result = lambda x: sorted(x, key=lambda x: sum(x))

#Write a Python program to extract specified size of strings from a give list of string values using lambda
l = ['Python', 'list', 'exercises', 'practice', 'solution']
#solution using list, filter and lambda
result = list(filter(lambda x : (len(x) == 8),l))
#Or a more dynamic approach
result = lambda x, y:list(filter(lambda x : (len(x) == y),x))
result(l, 8)
#using list comprehension
result = [x for x in l if len(x) == 4]

#SIDE NOTE: I noticed something that is curious. When passing a lambda function into a timer function
#the result is an object and not the return value of the time_it function. Not sure why
#need to investigate this.

#Write a Python program to count float numbers in a given mixed list using lambda.
#solution using list, filter and lambda
l = [1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
result = lambda x: list(filter(lambda x: (isinstance(x, float)), x))
print('There are {0} floats in the list which are: {1}'.format(len(result(l)), result(l)))
#using list comprehension
result = [x for x in l if isinstance(x, float)]

#Write a Python program to check whether a given string contains a capital letter, 
#a lower case letter, a number and a minimum length using lambda
#A solution using lambda and list comprehension
word = 'w3resource'
result = [lambda x, y:'{0} is a valid string'.format(x) if (any(chr.isdigit() for chr in x) and 
any(chr.upper() for chr in x) and any(chr.lower() for chr in x) and len(x) == y) else False]
result[0](word)
#W3resource solution: Really cool solution. Creative
def check_string(str1):
    messg = [
    lambda str1: any(x.isupper() for x in str1) or 'String must have 1 upper case character.',
    lambda str1: any(x.islower() for x in str1) or 'String must have 1 lower case character.',
    lambda str1: any(x.isdigit() for x in str1) or 'String must have 1 number.',
    lambda str1: len(str1) >= 7 or 'String length should be atleast 8.',]
    result = [x for x in [i(str1) for i in messg] if x != True]
    if not result:
        result.append('Valid string.')
    return result    
s = input("Input the string: ")
print(check_string(s))

#cool tip/ pays to really understand slicing
def every_nth(lst, nth):
  return lst[nth - 1::nth]#using slicing
print(every_nth([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))

#Problem 34: Write a Python program to filter the height and width of students,
#which are stored in a dictionary using lambda.

og_dict = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65),
           'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
#my solution
result = lambda x, y, z: dict(filter(lambda x: (x[1][0], x[1][1]) > (y, z), x))
result(og_dict.items(), 6, 70)
#W3bresource solution
def filter_data(students):
    result = dict(filter(lambda x: (x[1][0], x[1][1]) > (6.0, 70), students.items()))
    return result  
students = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
print("Original Dictionary:")
print(students)
print("\nHeight> 6ft and Weight> 70kg:")
print(filter_data(students))

#Write a Python program to check whether a specified list is sorted or not using
nums = [1, 2, 4, 6, 8, 10, 12, 14, 16, 17]

#My solution
is_sorted = [lambda x: 'This is a sorted list {0}'.format(x) if x == sorted(x) 
             else 'This list is not sorted {0}'.format(x)]
is_sorted[0](nums)

#w3resource soultion
def is_sort_list(nums, key=lambda x: x):
    for i, e in enumerate(nums[1:]):
        if key(e) < key(nums[i]): 
            return False
    return True
nums1 = [1,2,4,6,8,10,12,14,16,17]
print ("Original list:")
print(nums1)
print("\nIs the said list is sorted!")
print(is_sort_list(nums1)) 
nums2 = [2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,4,6,9,1,2]
print ("\nOriginal list:")
print(nums1)
print("\nIs the said list is sorted!")
print(is_sort_list(nums2))

#Write a Python program to extract the nth element from a given list of tuples using lambda
p = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
#My solution
nth = lambda x, n: list(map(lambda x:(x[n]), x))

#Write a Python program to sort a list of lists by a given index of the inner list using lambda.
students = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
#my solution
result = lambda x, y: list(sorted(x, key= lambda i:(i[y])))
result(students, 0)

#38Write a Python program to remove all elements from a given list present in another list using lambda
lst_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst_2 = [2, 4, 6, 8]
#Think first of
lst_1.remove(2)
lst_1.pop(index)
#clear will clear the entire list as in 
lst_1.clear()# just forgot about this one but not applicable to this solution

#My solution
result = lambda x, y: list(map(lambda n: (x.remove(n)),y))#using lambda

#w3resource solution
def index_on_inner_list(list1, list2):
    result = list(filter(lambda x: x not in list2, list1))
    return result
# A refined version
result = lambda x, y: list(filter(lambda n: n not in y, x))#An issue here which I see
#is that the w3resource soultion does not actually modify the original list. Which is fine if thats your aim. 


#39. Write a Python program to find the elements of a given list of strings 
#that contain specific substring using lambda.
#My solution 
colors = ['red', 'black', 'white', 'green', 'orange']
result = lambda x, y: list(filter(lambda n: (y in n), x))
print(result(colors, 'ack'))

#40 Write a Python program to find the nested lists elements, which are present in another list using lambda
lst_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
lst_2 = [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28],[1, 5, 8, 18, 15, 16]]

#Solution using list comprehension
result = [x for x in lst_2 for x in x if x in lst_1]

#w3resource solution
def intersection_nested_lists(l1, l2):
    result = [list(filter(lambda x: x in l1, sublist)) for sublist in l2]
    return result

#41 Write a Python program to reverse strings in a given list of string values using lambda.

l1 = ['Red', 'Green', 'Blue', 'White', 'Black']
#My solution
result = lambda x: [*map(lambda x: (x[::-1]),x)]
result(l1)

#Side challenge move the specified amount of elements to the end of the list. 
#solution
def tips_offset(lst, offset):
  return lst[offset:] + lst[:offset]

print(tips_offset([1, 2, 3, 4, 5, 6, 7, 8], 3)) 
print(tips_offset([1, 2, 3, 4, 5, 6, 7, 8], -3))


#42 Write a Python program to calculate the product of a given list of numbers using lambda
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#my solution
from functools import reduce
reduce(lambda a, b: a*b, l1)

#The solution without importing reduce from functools
def algo(func, num_list):
  x = num_list[0]#The 0th item in the list
  for i in range(1, len(num_list)):#The range is needed for accessing all of the indices of the list
    x = func(x,num_list[i])#The function is evaluated based off what x was in the previous loop iteration
    #Keep in mind x was something but it will also iteravely become something else and that thing
    #that it becomes will be the value of x in the function(x, list[i]) during the next iteration.
  return x #returns the final value of x after the loop has exhausted

def mult(a, b):
  return a*b

#43 is redundant the same as 42

#44 Write a Python program to calculate the average value of the numbers in a given tuple of tuples using lambda.
#I didnt understand this problem
nums = ((10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3))
#w3resource solution
result = tuple(map(lambda x: sum(x) / float(len(x)), zip(*nums)))
#modified
result = lambda x: tuple(map(lambda x: sum(x) / float(len(x)), zip(*x)))

#45. Write a Python program to convert string element to integer inside a given tuple using lambda.
l1 = (('233', 'ABCD', '33'), ('1416', 'EFGH', '55'), ('2345', 'WERT', '34'))

#w3resource solution
result = tuple(map(lambda x: (int(x[0]), int(x[2])), tuple_str))
#My solution using list comprehension
result = [x for x in l1 for x in x if x.isnumeric()]

#46. Write a Python program to find index position and value of the maximum and minimum values 
#in a given list of numbers using lambda.
#my solution
nums = [12,33,23,10.11,67,89,45,66.7,23,12,11,10.25,54]
result = lambda x: (max(enumerate(x), key=lambda x: x[1]), min(enumerate(x), key=lambda x: x[1]))
t = result(nums)
print('@ index position {0} max value {1} was found\n@ index position {2} min value {3} was found '.format(t[0][0],t[0][1],t[1][0],t[1][1]))
#47. Write a Python program to sort a given mixed list of integers and strings using lambda. Numbers must be 
#sorted before strings.
l1 = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
#my solution, in retrospec doesnt really do the job
result = lambda x: sorted(x, key= lambda y: (isinstance(y, str)))
#Better solution
result = lambda x: x.sort(key=lambda e: (isinstance(e, str), e))
#The above method will not print anything out but once the list is printed you will see it has been modified
#after calling the function and passing the list to it. 
result(l1)# like so
'''There is a really important thing going on here which needs be taken note of. The variable e is not x.
the reason is x is the list and this method is a list method so it is being applied to the stuff inside
the list. The sort method is already being applied to the list therfor its silly to try and pass it the
list where e is, e will be the stuff inside of x so passing the function is makes sense'''
#To note sorted does not effect the original sequence and x.sort() does
L = ['aaaa', 'bbb', 'cc', 'd']
 
# sorted without key parameter
print(sorted(L))
print()
 
# sorted with key parameter
print(sorted(L, key = len)) #Sorting by the length of something example

#Key takeaways, sorting returns a value and is not limited to lists wheras sort returns nothing but manipulates
#the original list.

#48. Write a Python program to sort a given list of strings(numbers) numerically using lambda.
l1 = ['4', '12', '45', '7', '0', '100', '200', '-12', '-500']
#The solution to this uses the other sorted method
result = lambda x: sorted(x, key=lambda e: int(e))

#49. Write a Python program to count the occurrences of the items in a given list using lambda
l1 = [3, 4, 5, 8, 0, 3, 8, 5, 0, 3, 1, 5, 2, 3, 4, 2]
#My solution
result = lambda x: list(map(lambda z: ('{0} FOUND '.format(z), ':{0}: TIMES'.format(list(x).count(z))),x))
#w3resource solution 
result = dict(map(lambda el: (el, list(nums).count(el)), nums))

#Takeaway: The list method doesnt work well in this situation because it allows multiples.
#For that reason set() and dict() are much better.

#50. Write a Python program to remove specific words from a given list using lambda
l1 = ['orange', 'red', 'green', 'blue', 'white', 'black']
#My solution
result = lambda x, *y: list(filter(lambda n:(n not in y), x))
result(l1, 'white', 'black')

#w3resource solution
def remove_words(list1, remove_words):
    result = list(filter(lambda word: word not in remove_words, list1))
    return result
    #Basically identical to my solution

#51. Write a Python program to find the maximum and minimum values in a given list of tuples using lambda function.
l1 = [('V', 62), ('VI', 68), ('VII', 72), ('VIII', 70), ('IX', 74), ('X', 65)]
#My first solution for this
result = lambda x: (max(x, key=lambda x: x[1])[1], min(x, key=lambda x: x[1])[1])
#Then
t = result(l1)
print(t[0][1], t[1][1])# Which shows the output like the output in w3resource
#or you could skip the line t = result[l1] and just
print('The maximum value is {0} and the minimum value is {1}'.format(result(l1)[0], result(l1)[1]))

#Another solution but very gnarly and not very efficient
r_max = lambda x: max(list(map(lambda y: (max(y, key=lambda y: isinstance(y, int))),x)))
#The min version of this is not a solution and does not work.
#I have had issues like this before using the min method I am not sure why it does not function the same
#as the max method. I need to investigate this.
r_min = lambda x: min(list(map(lambda y: (min(y, key=lambda y: isinstance(y, int))),x)))

#52. Write a Python program to remove None value from a given list using lambda function.
l1 = [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
#My solution
result = lambda x: list(filter(lambda y: (y != None), x))
print('Remove {1} values from said list: \n{0}'.format(result(l1), None))

#100 programming puzzles
#1. Write a Python program find a list of integers with exactly two occurrences of 
#nineteen and at least three occurrences of five.
l1 = [19, 19, 15, 5, 3, 5, 5, 2]
l2 = [19, 15, 15, 5, 3, 3, 5, 2]
l3 = [19, 19, 5, 5, 5, 5, 5]
#my solution
result = lambda x: (x.count(19) == 2 and x.count(5) >= 3)
#my other solution
result = lambda *x: list(map(lambda y: (y.count(19) == 2 and y.count(5) >= 3), x))
#Then you can pass more lists at once
result(l1, l2, l3)
#2. Write a Python program that accept a list of integers and check the length and 
#the fifth element. Return true if the length of the list is 8 and fifth element occurs thrice in the said
l1 = [19, 19, 15, 5, 5, 5, 1, 2]
l2 = [19, 15, 5, 7, 5, 5, 2]
#My solution
result = lambda x: (x.count(x[4]) == 3 and len(x) == 8)

#3 Write a Python program that accept an integer test whether an integer greater than 4^4 and which is 4 mod 34.
n1 = 922
n2 = 914
n3 = 854
result = lambda x: (x % 34 == 4 and x > 4 ** 4)

'''4. We are making n stone piles! The first pile has n stones. If n is even, then all piles have an even number of 
stones. If n is odd, all piles have an odd number of stones. Each pile must more stones than the previous pile but 
as few as possible. Write a Python program to'''

#w3resource solution
def test(n):    
    return [n + 2 * i for i in range(n)]

#5. Write a Python program to check the nth-1 string is a proper substring of nth string in a given list of strings
l1 = ['a', 'abb', 'sfs', 'oo', 'de', 'sfde']

l2 = ['a', 'abb', 'sfs', 'oo', 'ee', 'sfde']

#s3resource solution
def test(str1):
    return str1[len(str1)-2] in str1[len(str1)-1] and str1[len(str1)-2] != str1[len(str1)-1]

  #my solution
  result = lambda x: (x[-2] in x[-1])

#Quick slicing review
l1[::-1]#reverse the list
l1[::-2]#reverse list and get every 2nd item starting from the last item in the listl
l1[::2]# get every 2nd item in list starting from first item in list
l1[1::]# get the list but removes the first item
l1[2::]#gets the list but removes the 2nd item in the list
l1[-1]#gives you the last item in the list
l1[-2]#gives you the second to the last item in the list
l1[0:6:2] #gives you 0 - 6 in steps of 2

#6. Write a Python program to test a list of one hundred integers between 0 and 999,
#which all differ by ten from one another. Return true or false. Check item before

l1 = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 
      240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 
      460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 
      680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 
      900, 910, 920, 930, 940, 950, 960, 970, 980, 990]

l2 = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420, 440, 
      460, 480, 500, 520, 540, 560, 580, 600, 620, 640, 660, 680, 700, 720, 740, 760, 780, 800, 820, 840, 860, 880, 
      900, 920, 940, 960, 980]
#w3resource solution
def test(li):#This is a gnarly solution I cant really wrap my head around yet
    return all(i in range(1000) and abs(i - j) >= 10 for i in li for j in li if i != j) and len(set(li)) == 100

#My solution
result = lambda x: all(list(map(lambda y, z: (z - 10 == y),x,x[1::])))#I got clever here and used the same
#list twice where y is equal to the entire list and z is equal to the entire list after the first element

#7 Write a python program to test if the sum of elements in a given list is equal to the length of the list.
#This problem was worded very poorly on the w3resource website and its solution is wild

nums = [0,1,2,3,4,5]

#w3resource solution
def test(nums):
    return all([sum(nums[:i]) == i for i in range(len(nums))])

#my solution
result = lambda x: (sum(x) == len(x))

#8. Write a Python program to split a string of words separated by commas and spaces into two lists, 
#words and separators.
str1 = 'W3resource Python, Exercises.'
str2 = ' The colors in my studyroom are blue, green, and yellow.'
str3 = 'The dance, held in the school gym, ended at midnight.'

#Solution
merged = lambda x: sorted(re.split(r"([ ,]+)", x), reverse=True)

#w3resource solution #Study this one alot the regex module is new to me
import re
def test(string):
    merged = re.split("([ ,]+)", string)
    return [merged[::2], merged[1::2]]

#9. Write a Python program to find list integers containing exactly four distinct values, such that 
#no integer repeats twice consecutively among the first twenty entries.
l1 = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
l2 = [1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3]
l3 = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
l4 =  [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 3, 1, 2, 3, 3]

#My solution
result = lambda x: (len(set(x)) == 4)
result = lambda x: all([x[i] != x[i + 1] for i in range(len(x)-1)]) and len(set(x)) == 4
result = lambda x: all(map(lambda y, z: (y != z and len(set(x)) == 4),x,x[1::]))

#w3resource solution
def test(nums):
    return all([nums[i] != nums[i + 1] for i in range(len(nums)-1)]) and len(set(nums)) == 4

#Dont forget to look up .get and learn regex really well and the walrus operator

#10 iven a string consisting of whitespace and groups of matched parentheses, write a 
#Python program to split it into groups of perfectly matched parentheses without any whitespace.
combined = '( ()) ((()()())) (()) ()'
def test(combined):
   ls = []
   s2 = ""
   for s in combined.replace(' ', ''):
       s2 += s
       if s2.count("(") == s2.count(")"):
           ls.append(s2)
           s2 = ""
   return ls

#11. Write a Python program to find the indexes of numbers of a given list below a given threshold.
l1 = [(100,(0, 12, 45, 3, 4923, 322, 105, 29, 15, 39, 55))]# 100 is the threshold in this example
#A solution using list comprehension
result = [x for x, y in enumerate(l1[0][1]) if y < 100]
#A more dynamic flavor of the previous solution now as a function with list comprehension
result = lambda x, z: [x for x, y in enumerate(x) if y < z]
result(l1[0][1], l1[0][0])

#12. Write a Python program to check whether the given strings are palindromes or not. Return True, False.
p = ['palindrome', 'madamimadam', '', 'foo', 'eyes']
#My solution
result = lambda x: [True if x and x == x[::-1] else False for x in x]

#13. Write a Python program to find the strings in a given list, starting with a given prefix.
l1 = [( 'ca',('cat', 'car', 'fear', 'center'))]
l2 = [('do',('cat', 'dog', 'shatter', 'donut', 'at', 'todo'))]
#My solution
result = lambda x: [y for x, y in zip(x[0][0], x[0][1]) if x in y]#Not a solution
#I solved this before using this
result = lambda x, y: list(filter(lambda n: (n.startswith(y)), x))
#Then
result(l1[0][1], l1[0][0]) or result(l2[0][1], l2[0][0])

#14. Write a Python program to find the lengths of a given list of non-empty strings.
l1 = ['cat', 'car', 'fear', 'center']
l2 = ['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
l3 = ['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '', ['cat', 'car', 'fear', 'center']]
#my solution
result = lambda x: [len(x) for x in x]

#w3resource solution is cool too
result = lambda x: [*map(len, x)]
  #This is pretty clever because instead of making a list we can tell the interpreter
  #simply to unpack the map using *. 

#15. Write a Python program find the longest string of a given list of strings
l1 = ['cat', 'car', 'fear', 'center']
#Solution
result = lambda x: max(x, key=len)

#16. Write a Python program find the strings in a given list containing a given substring
l1 = [( 'ca',('cat', 'car', 'fear', 'center'))]
l2 = [('do',('cat', 'dog', 'shatter', 'donut', 'at', 'todo'))]
l3 = [('o',('cat', 'dog', 'shatter', 'donut', 'at', 'todo', ''))]
#My solution
result = lambda x, y: [*filter(lambda n: (y in n), x)]

#17. Write a Python program to create a string consisting of the non-negative integers up to n inclusive.
n = 15
#solution
result = lambda x: ' '.join(map(str, range(n+1)))

'''18. An irregular/uneven matrix, or ragged matrix, is a matrix that has a different number of elements in each row. 
Ragged matrices are not used in linear algebra, since standard matrix transformations cannot be performed on them, 
but they are useful as arrays in computing.
Write a Python program to find the indices of all occurrences of a target in the uneven matrix.'''
m = [[1, 3, 2, 32, 19], [19, 2, 48, 19], [], [9, 35, 4], [3, 19]]
t = 19
result = lambda x, y: [[z, w] for z, f in enumerate(x) for w, v in enumerate(f) if y == v]
result(m, t)

# #19. Write a Python program to split a given string (s) into strings if there is a space in the string, otherwise 
# split on commas if there is a comma, otherwise return the list of lowercase letters with odd order 
# (order of a = 0, b = 1, etc.)
s1 = 'a b c d'
s2 = 'a,b,c,d'
s3 = 'abcd'

#My solution
result = lambda x: x.split() if ' ' in x else x.split(',') if ',' in x else x[1::2]

#20.Write a Python program to determine the direction ('increasing' or 'decreasing') of monotonic sequence numbers.

l1 = [1, 2, 3, 4, 5, 6]

l2 = [6, 5, 4, 3, 2, 1]

l3 = [19, 19, 5, 5, 5, 5, 5]

a = ['Increasing.', 'Decreasing', 'Not a monotonic sequence!']
#My solution
result = lambda x, a: [*map(lambda y, z: a[0] if y == z-1 else a[1] if y == z+1 else a[2], x, x[1::])]

#w3resource solution
def test(nums):
    return "Increasing." if all(nums[i] < nums[i + 1] for i in range(len(nums) - 1)) else \
        "Decreasing." if all(nums[i + 1] < nums[i] for i in range(len(nums) - 1)) else \
        "Not a monotonic sequence!"

#21. Write a Python program to check, for each string in a given list, whether the last 
#character is an isolated letter or not. Return True or False.

l1 = ['cat', 'car', 'fear', 'center']
l2 = ['ca t', 'car', 'fea r', 'cente r']

#My solution
result = lambda x: [*map(lambda a: (' ' == a[-2]), x)]


#22. Write a Python program to compute the sum of the ASCII values of the upper-case characters in a given string.

#use
ord()#which takes an argument in the form of a single character

s1 = 'PytHon ExerciSEs'
s2 = 'JavaScript'

result = lambda x: sum([ord(i) for i in x if i.isupper()])

#w3resource solution
result = sum(map(ord,filter(str.isupper,strs)))#cool solution

#23. Write a Python program to find the indices for which the numbers in the list drops

l1 = [0, -1, 3, 8, 5, 9, 8, 14, 2, 4, 3, -10, 10, 17, 41, 22, -4, -4, -15, 0]
l2 = [6, 5, 4, 3, 2, 1]
l3 = [1, 19, 5, 15, 5, 25, 5]
result = lambda x: [[z[0]+1, y] for z, y in zip(enumerate(x), x[1::]) if y < z[1]]
#Or just the indices
result = lambda x: [z[0]+1 for z, y in zip(enumerate(x), x[1::]) if y < z[1]]

#w3resource solution
def test(nums):
    return [i for i in range(1, len(nums)) if nums[i] < nums[i - 1]]#Review this solution as I dont use range enough

#24. Write a Python program to create a list whose ith element is the 
#maximum of the first i elements from a input list.

l1 = [0, -1, 3, 8, 5, 9, 8, 14, 2, 4, 3, -10, 10, 17, 41, 22, -4, -4, -15, 0]
#output should be
output = [0, 0, 3, 8, 8, 9, 9, 14, 14, 14, 14, 14, 14, 17, 41, 41, 41, 41, 41, 41]

#my solution
result = lambda x: [max(x[:z]) for z in range(1, len(x))]
#or
result = lambda x: list(map(lambda y: (max(x[:y])), range(1, len(x))))
#or
result = lambda x: [*map(lambda y: (max(x[:y])), range(1, len(x)))]

#25. Write a Python program to find the XOR of two given strings interpreted as binary numbers.

l1 = ['0001', '1011']
l2 = ['100011101100001', '100101100101110']

#My solution
result = lambda x: (bin(int(x[0], 2)^int(x[1], 2)))#Review operators and nth complexity


#26. Write a Python program to find the largest number where commas or periods are decimal points.

l1 = ['100', '102,1', '101.1']
result = lambda x: max([s.replace(',', '.') for s in x])

#w3resource solution
def test(str_nums):
    return max(float(s.replace(",", ".")) for s in str_nums)

''' Squared deviations from the mean (SDM) are involved in various calculations. In probability theory and statistics,
the definition of variance is either the expected value of the SDM (when considering a theoretical distribution)
or its average value (for actual experimental data). Computations for analysis of variance involve the partitioning
of a sum of SDM. '''
#27. Write a Python program to find x that minimizes mean squared deviation from a given a list of numbers.
#The problem requires minimizing the sum of squared deviations, which turns out to be the mean mu. Moreover,
#if mu is the mean of the numbers then a simple calculation.
l1 = [4, -5, 17, -9, 14, 108, -9]

l2 = [12, -2, 14, 3, -15, 10, -45, 3, 30]

#w3resource solution
def test(nums):
    return sum(nums) / len(nums)

#28. Write a Python program to select a string from a given list of strings with the most unique characters.

l1 = ['cat', 'catatatatctsa', 'abcdefhijklmnop', '124259239185125', '', 'foo', 'unique']
l2 = ['Green', 'Red', 'Orange', 'Yellow', '', 'White']
#my solution
max(l1, key= lambda x: [*map(lambda y: (y[1:] != y),x)])
#w3resource solution
result = lambda x: max(x, key=lambda y: len(set(y))) #more elegant actlly

#29. Write a Python program to find the indices of two numbers that sum to 0 in a given list of numbers.
l1 = [1, -4, 6, 7, 4]
l2 = [1232, -20352, 12547, 12440, 741, 341, 525, 20352, 91, 20]
#w3resource solution
def test(nums):
    s = set(nums)
    for i in s:
        if -i in s:
            return [nums.index(i), nums.index(-i)]

#my solution
result = lambda x: [(x.index(i)) for i in set(x) if -i in x] #Think about this one again


#30. Write a Python program to find the list of strings that has fewer total characters (including repetitions)
l1 = [['this', 'list', 'is', 'narrow'], ['I', 'am', 'shorter but wider']]
l2 = [['Red', 'Black', 'Pink'], ['Green', 'Red', 'White']]
#w3resource solution
def test(strs):
    return min(strs, key=lambda x: sum(len(i) for i in x))

#31. Write a Python program to find the coordinates of a triangle with the given side lengths.
l1 = [3, 4, 5]

#w3resource solution
def test(sides):
   a, b, c = sorted(sides)
   s = sum(sides) / 2 # semi-perimeter
   area = (s * (s - a) * (s - b) * (s - c)) ** 0.5 # Heron's formula
   y = 2 * area / a # height
   x = (c ** 2 - y ** 2) ** 0.5
   return [[0.0, 0.0], [a, 0.0], [x, y]]
#32. Write a Python program to rescale and shift numbers of a given list, so that they cover the range [0, 1]
l1 = [18.5, 17.0, 18.0, 19.0, 18.0]
#w3resource solution
def test(nums):
    a = min(nums)
    b = max(nums)
    if b - a == 0:
        return [0.0] + [1.0] * (len(nums) - 1)
    for i in range(len(nums)):
        nums[i] = (nums[i] - a) / (b - a)
    return nums

#33. Write a Python program to find the positions of all uppercase vowels (not counting Y) in even indices 
#of a given string.

s = 'w3rEsOUrcE'
#my solution
vowels = [x for x, y in enumerate(s) if y in ['A', 'E', 'I', 'O', 'U'] and x%2 == 0]
#or more dynamic
vowels = lambda s: [x for x, y in enumerate(s) if y in 'AEIOU' and x%2 == 0]

#34. Write a Python program to find the sum of the numbers of a given list among the first k with 
#more than 2 digits.
l1 = [114, 215, -117, 119, 14, 108, -9, 12, 76]
k = 5
#My solution
sumthin = lambda x, y: sum([n for n in x[:y] if len(str(abs(n))) > 2])

#w3resource solution
def test(nums, k):
    s = 0
    for i in range(len(nums))[:k]:
        if len(str(abs(nums[i]))) > 2:
            s = s + nums[i]
    return s

#Write a Python program to compute the product of the odd digits in a given number, or 0 if there aren't any.
l1 = 123456789
l2 = 2468

mult = lambda a, b: a*b

def algo(func, num_list):
  odds = lambda nums: [int(x) for x in str(nums) if int(x)% 2 == 1]
  x = odds(num_list)[0]
  for i in range(1, len(odds(num_list))):
    x = func(x,odds(num_list)[i])
  return x
odds = lambda num_list: [int(x) for x in str(l1) if int(x)% 2 == 1]

#w3resource solution
def test(n):
    if any(int(c) % 2 for c in str(n)):
        prod = 1
        for c in str(n):
            if int(c) % 2 == 1:
                prod *= int(c)
        return prod
    return 0
result = lambda x:
#36. Write a Python program to find the largest k numbers from a given list of numbers
n = 1
l1 = [1, 2, 3, 4, 5, 5, 3, 6, 2]
#My solution
def large(number, a_list):
  b = a_list.copy()
  a = []
  while range(number):
    a.append(max(b))
    b.remove(max(b))
    number -= 1
  return a

#w3resource solution
def test(nums, k):
    if k == 0:
        return []
    return sorted(nums, reverse=True)[:k]

#Improved
result = lambda nums, n: sorted(nums, reverse=True)[:n] if n else 0

#37. Write a Python program to find the largest integer divisor of a number n that is less than n
#My solution
result = lambda n: int(n / 2) if n > 0 else ValueError('n Must be larger than 0 pal')

#w3resource solution
def test(n):
     return next(d for d in range(n - 1, 0, -1) if n % d == 0)
#38. Write a Python program to sort the numbers of a given list by the sum of their digits.
l1 = [23, 2, 9, 34, 8, 9, 10, 74]
#My solution
result = lambda x: sorted(x, key=lambda y: sum([int(i) for i in str(y) if i != '-']))

#39 Write a Python program to determine which triples sum to zero from a given list of lists.
l1 = [[1343532, -2920635, 332], [-27, 18, 9], [4, 0, -4], [2, 2, 2], [-20, 16, 4]]
#My solution which produces the actual lists which sum to 0
result = lambda x: [i for i in x if sum(i) == 0]
#My solution which produces the same results as the w3resource output 
result = lambda x: [*map(lambda y: (sum(y) == 0), x)]
#w3resource solution
def test(nums):
    return [sum(t)==0 for t in nums]# Notice: there is an expression for the return result in the list comprehension

#40. Write a Python program to find string s that, when case is flipped gives target
# where vowels are replaced by chars two later.
#Worded terribly.
#Better wording:
#Write a python program which inverts each letters case in a string and replaces vowels with consonants two
#letters down from the vowel.
l1 = 'Hello, world!'
#w3resource solution
def test(strs):
     return strs.translate({ord(c):ord(c)+2 for c in "aeiouAEIOU"}).swapcase()

#The maketrans method and the translate method
string = 'a te(sting$*'
str1 = 'abcde'
str2 = '12345'
str3 = '$(*'
t = string.maketrans(str1, str2, str3)# str1 are the characters we want replace with str2 characters.
#str 3 are the characters we want deleted all together.
#All the maketrans method does is create a table to be used with the translate method.
'''1st example!!'''
dict1 = {'a':'o', 't':'y', 'a':'1', 'g':'5'}
table = string.maketrans(dict1)
string.translate(table)

#second
string.translate(t)

#With all this in mind
result = lambda x: x.translate({ord(s):ord(s)+2 for s in 'aeiouAEIOU'}).swapcase()



#41. Write a Python program to sort numbers based on strings.
l1 = 'six one four one two three'
dict1 = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
#Rough solution but works
for x, y in enumerate(l1.split(' '), start=1):
  if dict1[x] in l1.split(' '):
    print(dict1[x])

#A refined solution but a bit gnarly
result = lambda x, y: [y[i] for i, s in enumerate(x.split(), start=1) if y[i] in x]

#w3resource solution
def test(strs):
    return ' '.join([x for x in 'one two three four five six seven eight nine'.split() if x in strs])
#I really like their solution because it doesnt involve the extra step of making a dictionary
#with key value pairs to iterate through. In addition this solution returns a string as opposed to a list.

#42. Write a Python program to find the set of distinct characters in a given string, ignoring case.

l1 = 'HELLO'
l2 = 'HelLo'
l3 = 'Ignoring case'

#My solution
result = lambda x: set(x.lower())
#or 

result = lambda x: set(x.casefold())#casefold is more aggressive then .lower()

#Side problem
#A father dies that has 7 children. The father leaves his fortune x to his 7 children. Each child is favored
#differently and thus each is child recieves a different percentage of the inheratance.
#child 1: 30%, child 2: 20%, child 3: 15%, child 4: 10%, child 5: 10%, child 6: 8%, child 7: 7%

#First given the individual percentage per child distribute the inheritance among them. Then
#kill off a child of your choosing and redistribute that childs inheritance among the surviving children
#taking into account each childs original percentage adjusted now. Build a program that automates this process


q = 300000
kids = {'a1': .3*q, 'b1': .2*q, 'c1': .15*q, 'd1': .1*q, 'e1': .08*q, 'f1': .07*q, 'g1': .1*q}
z = kids['c1']
s_kids = {'a2': (q*kids['a1']) / (q - z), 'b2': (q*kids['b1']) / (q - z), 
                'd2': (q*kids['d1']) / (q - z), 'e2': (q*kids['e1']) / (q - z),
                'f2': (q*kids['f1']) / (q - z), 'g2': (q*kids['g1']) / (q - z)}
#43. Write a Python program to find all words in a given string with n consonants.
l1 = 'this is our time'
consonants = 'bcdfghjklmnpqrstvwxyz'
vowels = 'aeiouAEIOU'
result = lambda x:[*filter(lambda i: len(i) == 3,''.join([s for s in x if s not in 'aeiouAEIOU']).split())]
result = lambda x: [*filter(lambda i: max(i) in ,x.split())]
result = lambda x: [*filter(lambda i: 'bcdfghjklmnpqrstvwxyz'.count(i), x.split())]
result = [w for w in strs.split() if sum([c not in "aeiou" for c in w.lower()]) == n]


#44. Write a Python program to find which characters of a hexadecimal number correspond to prime numbers.
def test(hn):
    return [c in "2357BD" for c in hn]
l1 = '123ABCD'

#45. Write a Python program to find all even palindromes up to n.
n = 100

result = lambda x: [k for k in range(n) if str(k)[::-1] == str(k) and k%2 == 0]




#46. Given an array of numbers representing a branch on a binary tree, write a Python program to find the minimum 
#even value and its index. In the case of a tie, return the smallest index. If there are no even numbers, the answer 
#is []. 

def test(nums):
    if any(n % 2 == 0 for n in nums):
        return min([v, i] for i, v in enumerate(nums) if v % 2 == 0)
    else:
        return []

#47. Write a Python program to Filter for the numbers in numbers in a given list whose sum of digits is > 0, where 
#the first digit can be negative
'''So the individual numbers in each element need to add up to a sum greater then 0'''
l1 = [11, -6, -103, -200]
def grt(lst):
  for x in lst:
    print(sum([int(str(x)[l]) for l in range(len(str(x))) if str(x)[l] != '-']))
    sum([int(str(x)[l]) if str(x)[l] != '-' else -int(str(x[1])) for l in range(len(str(x)))])


def grt(lst):
  for x in lst:
    for l in range(len(str(x))):
      if str(x)[l] != '-':
        print(sum([int(str(x)[l])]))

#w3resource solution
def test(nums):
    return [n for n in nums if int(str(n)[:2]) + sum(map(int, str(n)[2:])) > 0]

#48. Write a Python program to find the indices of two entries that show that the list is not in increasing order. 
#If there are no violations (they are increasing), return an empty list.

l1 = [1, 2, 3, 0, 4, 5, 6]#output should be [2,3]
l2 = [1, 2, 3, 4, 5, 6]#output should be [] or 'List Increasing'

result = lambda n: [(y[0], x[0]+1) if y[1] >= x[1] else 'List Increasing' for x, y in zip(enumerate(n[1:]), enumerate(n))]
#or
result = lambda n: [(y[0], x[0]+1) for x, y in zip(enumerate(n[1:]), enumerate(n)) if y[1] >= x[1]]

#w3resource solution
def test(nums):
    for i in range(len(nums) - 1):
        if nums[i] >= nums[i + 1]:
            return [i, i + 1]
    return []

#49. Write a Python program to find the h-index, the largest positive number h such that h occurs in the sequence at least
#h times. If there is no such positive number return h = -1

l1 = [1, 2, 2, 3, 3, 4, 4, 4, 4]#output should be 4

l2 = [1, 2, 2, 3, 4, 5, 6]#output should be 2
l3 = [3, 1, 4, 17, 5, 17, 2, 1, 41, 32, 2, 5, 5, 5, 5]
l4 = [3, 3, 2, 9, 6, 7, 7, 7, 2]

def test(lst):
  for x in lst:
    if x >= 0 and lst.count(x) == x and x == max(lst):
      print(x)
#Simplified
result = lambda lst: [x  if x >= 0 and lst.count(x) == x and x == max(lst) else 'h = -1' for x in lst]

def test(lst):
  return max(lst, key=lambda x: lst.count(x))

#50. Write a Python program to find the even-length words from a given list of words and sort them by length.
l1 = ['Red', 'Black', 'White', 'Green', 'Pink', 'Orange']
l2 = ['The', 'worm', 'ate', 'a', 'bird', 'imagine', 'that', '!', 'Absurd', '!!']
result = lambda x: sorted([s for s in x if len(s)%2 == 0], key=lambda x: (len(x),x))

#51. Write a Python program to find the first n Fibonacci numbers.
n = 10
def fib(num):
  a = [0, 1]
  while len(a) < num: a += [sum(a[-2:])]
  return a

#52. Write a Python program to reverse the case of all strings. For those strings, which contain no letters, 
#reverse the strings.

l1 = ['cat', 'catatatatctsa', 'abcdefhijklmnop', '124259239185125', '', 'foo', 'unique']
l2 = ['Hello', '!@#', '!@#$', '123#@!']
l3 = ['Green', 'Red', 'Orange', 'Yellow', '', 'White']
#My solution
result = lambda x: [x[s][::-1] if x[s].isnumeric() else x[s].swapcase() for s in range(len(x))]

#53. Write a Python program to find the product of the units digits in the numbers of a given list.
#(product of the last digits of each number in a list)
l1 = [12, 23]
l2 = [12, 23, 43]
l3 = [113, 234]
def prd(nums):
  a = 1
  for x in range(len(nums)):
    a = a*int(str(nums[x])[-1])
  return a


#w3resource solution
def test(nums):
     return eval('*'.join([str(x % 10) for x in nums]))

#54. Write a Python program to remove duplicates from a list of integers, preserving order.
l1 = [1, 3, 4, 10, 4, 1, 43]
l2 = [10, 11, 13, 23, 11, 25, 23, 76, 99]

#w3resource solution
def test(nums):
    return list(dict.fromkeys(l1))

result = lambda x: list(dict.fromkeys(x))

#55. Write a Python program to find the numbers that are greater than 10 and have odd first and last digits.
l1 = [1, 3, 79, 10, 4, 1, 39, 62]
l2 = [11, 31, 77, 93, 48, 1, 57]

result = lambda x: [n for n in x if n > 10 and int(str(n)[0]) % 2 and int(str(n % 10)) % 2]

#w3resource solution
def test(nums):
      return [x for x in nums if x > 10 and x % 10 % 2 and int(str(x)[0]) % 2]

#56. Write a Python program to find an integer exponent x such that a^x = n.

#The straight forward way of doing it.
a = 2
n = 1024

a = 3
n = 81

a= 3
n = 1290070078170102666248196035845070394933441741644993085810116441344597492642263849

#My solution
def find_exp(num, result):
  exponent = 0
  while num**exponent != result: exponent += 1
  return exponent

#w3resource solution
def test(n,a):
    m = 1
    x = 0
    while m != n:
        x += 1
        m *= a
    return x

#Playing with a concept
result = lambda n, result: [x for x in range(1000) if n**x == result]

#57. Write a Python program to find the sum of the magnitudes of the elements in the
#array with a sign that is equal to the product of the signs of the entries.

l1 = [1, 3, -2]
l2 = [1, -3, 3]
l3 = [10, 32, 3]
l4 = [-25, -12, -23]
l5 = [-25, 12, -23]
l6 = [5, 0, -9, 33]
result = lambda l: ''.join(str([[-1] if x < 0 else [abs(x)] for x in l])).replace('[','(').replace(']',')').replace(',','+').replace('-1','*-1')

#Gnarly solution but reliable
result = lambda l: ''.join(str([abs(x) for x in l])).replace('[',
'(').replace(']',')').replace(',',
'+')+''.join(str(['*-1' for x in l if x < 0])).replace('[',
'').replace(']','').replace("'",'').replace(',','')

#After a few mins of thinking... A better solution also reliable
result = lambda l: eval(''.join(['-1*' for x in l if x < 0])+str(sum(abs(x) for x in l)))

#w3resource solution
def test(nums):
    tot = sum(abs(i) for i in nums)
    if all(nums):
        return tot if sum(i < 0 for i in nums) % 2 == 0 else -tot
    return 0
#Some doods solution
def test(l):
    sign = 1
    sum = 0
    for v in l:
        if v < 0:
            sign *= -1
            sum += abs(v)
        else:
            sum += v
    return sum * sign

#58. Write a Python program to find the biggest even number between two numbers inclusive.

m = 12
n = 51
# Output:50
# Input:
m = 1
n = 79
# Output:78
# Input:
m = 47
n = 53
# Output:52
# Input:
m = 100
n = 200
# Output:200
max(range(n+1)[::-1], key=lambda x: x%2 == 0)
#My solution
result = lambda n: max(range(n+1)[::-1], key=lambda x: x%2 == 0)#<---- one character less than doods solution

#Some doods solution
def test(m, n):
  return max(v for v in range(m, n+1) if v % 2 == 0)
#The way I would write it..
result = lambda m, n: max(v for v in range(m, n+1) if v % 2 == 0)

#w3resource solution
def test(m, n):
    if m > n or (m == n and m % 2 == 1):
        return -1
    return n if n % 2 == 0 else n - 1

#59. A valid filename should end in .txt, .exe, .jpg, .png, or .dll, and should have at most three digits,
#no additional periods. Write a Python program to create a list of True/False that determine whether candidate
#filename is valid or not
l1 = ['abc.txt', 'windows.dll', 'tiger.png', 'rose.jpg', 'test.py', 'win32.exe']
l2 = ['.txt', 'windows.exe', 'tiger.jpeg', 'rose.c', 'test.java']

result = lambda s: [*map(lambda n: (n[-4:] in ['.txt','.exe','.jpg','.png','.dll'] and n.count('.') == 1 and sum(c.isdigit() for c in n) <= 3 and len(n) >= 5), s)]

def test(file_names):
         return ["Yes" if
            f.split(".")[1:] in [['txt'], ['png'],
             ['dll'], ['exe'], ['jpg']] and f[0].isalpha() and sum(c.isdigit() for c in f) < 4
            else "No"
            for f in file_names]


#60. Write a Python program to find a list of all numbers that are adjacent to a prime number 
#in the list, sorted without duplicates.
#Input:
l1 = [2, 17, 16, 0, 6, 4, 5]
#Output:
[2, 4, 16, 17]
#Input:
l2 = [1, 2, 19, 16, 6, 4, 10]
#Output:
[1, 2, 16, 19]
#Input:
l3 = [1, 2, 3, 5, 1, 16, 7, 11, 4]
#Output:
[1, 2, 3, 4, 5, 7, 11, 16]

l4= [0, 0, 1, 2, 5, 14, 15, 17, 19, 41, 0]

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

result = lambda x: list(dict.fromkeys([x[z] for z in range(len(x)) if x[z+1] % 2 and x[z+1] % 3 or x[z-1] % 2 and x[z-1] % 3 or x[z+1] in [1,2,3] or x[z-1] in [1,2,3]]))

#I need to use the range method twice. One list needs to be a rang of the list without the first and last item
#The second range needs to be used to check the first and last item in the list.
#zip is likely going to be needed

def test(nums):


index()


#w3resource solution
def test(nums):
    return sorted({
        n for i, n in enumerate(nums)
        if (i > 0 and prime(nums[i - 1])) or (i < len(nums) - 1 and prime(nums[i + 1]))
    })
    
def prime(m):
  if (m>0):
    return all(m % i for i in range(2, m - 1))



result =lambda x: [s for s in x if x.index(s) > 0 s%2 and s%3 or s in [123]]

#Lets use this as another example of this concept
#Make a program that returns all of the elements in a list next to vowels.
l6 = ['c', 'b', 'l', 'o', 'd', 'a', 'e', 'p']

result = lambda x: [n for i, n in enumerate(x) if (i > 0 and x[i-1] in ['a','e',
                    'i','o','u']) or (i < len(x) -1 and x[i+1] in ['a','e','i','o','u'])]

result = lambda x: [c for i, c in enumerate(x) if (i > 0 and all(x[i - 1] % r for r in range(2, x[i - 1] - 1))) or (i < len(x) - 1 and all(x[i + 1] % r for r in range(2, x[i - 1] - 1)))]

#61. Write a Python program to find the number which when appended to the list makes the total 0.

l1 = [1, 2, 3, 4, 5]
l2 = [-1, -2, -3, -4, 5]
l3 = [10, 42, 17, 9, 1315182, 184, 102, 29, 15, 39, 755]

result = lambda x: sum(x) * -1


#62. Write a Python program to find the dictionary key whose case is different than all other keys. 

l1 = {'red': '', 'GREEN': '', 'blue': 'orange'}
l2 = {'RED': '', 'GREEN': '', 'orange': '#125GD'}

#My solution
def case(d):
  result = [s for s in d if s.isupper()]
  if len(result) > 1:
    d = [s for s in d if s not in result]
  else:
    d = result
  return d[0]

#w3resource solution
def test(keys):
    for key in keys:
        if all(k.islower() != key.islower() for k in keys if k != key):
            return key


#63. Write a Python program to find the sum of the even elements that are at odd indices in a given list.
l1 = [1, 2, 3, 4, 5, 6, 7]
Output = 12
l2 = [1, 2, 8, 3, 9, 4]
Output = 6

#My solution
result = lambda x: sum([e for e in x if x.index(e)%2 and e%2 == 0])

#w3resource solution
def test(nums):
    return sum(i for i in nums[1::2] if i % 2 == 0)



#64. Write a Python program to find the string consisting of all the words whose lengths are prime numbers.
l1 = "The quick brown fox jumps over the lazy dog."
Output = "The quick brown fox jumps the"
l2 = "Omicron Effect: Foreign Flights Won't Resume On Dec 15, Decision Later."
Output = "Omicron Effect: Foreign Flights Won't On Dec 15,"

#My solution
result = lambda x: ' '.join([e for e in x.split() if len(e)%2 and len(e)%3 or len(e) in [1,2,3]])

#Know the bible better and biblical stories better

#w3resource solution
def test(strs):
    return " ".join(strs for strs in strs.split() if is_prime(len(strs))) 
def is_prime(n):
    return n > 1 and all(n % j for j in range(2, int(n ** 0.5) + 1))


#65. Write a Python program to shift the decimal digits n places to the left, 
#wrapping the extra digits around. If shift > the number of digits of n, reverse the string.

#Input:
n = 12345 and shift = 1
Output = 23451
#Input:
n = 12345 and shift = 2
Output = 34512
#Input:
n = 12345 and shift = 3
Output = 45123
#Input:
n = 12345 and shift = 5
Output = 12345
#Input:
n = 12345 and shift = 6
Output = 54321

#My solution
result = lambda x, y: int(str(x)[y:]+str(x)[:y]) if y <= len(str(x)) else int(str(x)[::-1])

#w3resource solution
def test(n, shift):
    s = str(n)
    if shift > len(s):
        return s[::-1]
    return s[shift:] + s[:shift]


#66. Write a Python program to find the indices of the closest pair from a list of numbers.

l1 = [1, 7, 9, 2, 10]
Output = [0, 3]
l2 = [1.1, 4.25, 0.79, 1.0, 4.23]
Output = [4, 1]
l3 = [0.21, 11.3, 2.01, 8.0, 10.0, 3.0, 15.2]
Output = [2, 5]

def sub(nums):
  e = sorted(nums.copy())
  d = {}
  for x in range(len(nums)-1):
    if abs(e[0]-e[1]) not in d.keys() and e[0]-e[1]:
      d[abs(e[0]-e[1])] = [e[0], e[1]]
      e.pop(0)
  return [nums.index(d[min(d)][0]), nums.index(d[min(d)][1])]

#67. Write a Python program to find a string which,
#when each character is shifted (ASCII incremented) by shift, gives the result.
l1 = 'Ascii character table'

result = lambda x, shift: ''.join([chr(ord(s)+shift) for s in x])

#68. Write a Python program to find all 5's in integers less than n that are divisible by 9 or 15.
n = 50
l1 = [[15, 1], [45, 1]]

def test(n):
    return [[i,j] for i in range(n) for j in range(len(str(i))) if str(i)[j] == '5' and (i%15==0 or i%9==0)]

#69. Write a Python program to create a new string by taking a string,
#and word by word rearranging its characters in ASCII order.
l1 = 'Ascii character table'
l2 = 'maltos won'

result = lambda x: ' '.join(''.join(sorted(s)) for s in x.split())

#70. Write a Python program to find the first negative balance from a given a list of numbers which
#represent bank deposits and withdrawals.

l1 = [[12, -7, 3, -89, 14, 88, -78], [-1, 2, 7]]
Output = [-81, -1]
l2 = [[1200, 100, -900], [100, 100, -2400]]
Output = [None, -2200]


def ledger(transactions):
  debt = []
  for entry_sheet in transactions:
    for i in range(len(entry_sheet)+1):
      if sum(entry_sheet[:i]) < 0:
        debt.append(sum(entry_sheet[:i]))
        break
    else:
      debt.append(None)
  return debt
#You really need to understand inner functions better and concepts like whether or not you can
#use a break statement before or after a return statement and what is the best way to
#return the inner function from the outer.

'''Combines two lists into a dictionary,
where the elements of the first one serve as the keys and the elements of the second one serve as the values. 
The values of the first list need to be unique and hashable:

Example:

def tips_to_dictionary(keys, values):
  return {key:value for key, value in zip(keys, values)}
print(tips_to_dictionary(['x', 'y'], [5, 10])) 
output = {'x': 5, 'y': 10}
'''
#77. Write a Python program to convert GPAs to letter grades according to the following table:
#4.0 and above = A+
#3.7 and above = A
#3.4 and above = A-
#3.0 and above = B+
#2.7 and above = B
#2.4 and above = B-
#2.0 and above = C+
#1.7 and above = C
#1.4 and above = C-
#Anything lower then 1.4 is an F

def grade(score):
  c = 'C+' if score >= 2.0 else 'C' if score >= 1.7 else 'C-' if score >= 1.4 else 'F'
  b = 'B+' if score >= 3.0 else 'B' if score >= 2.7 else 'B-' if score >= 2.4 else c
  a = 'A+' if score >= 4.0 else 'A' if score >= 3.7 else 'A-' if score >= 3.4 else b
  return a

#78. Write a Python program to find the two closest distinct numbers in a given a list of numbers. Go to the editor
l1 = [1.3, 5.24, 0.89, 21.0, 5.27, 1.3]
Output= [5.24, 5.27]
l2 = [12.02, 20.3, 15.0, 19.0, 11.0, 14.99, 17.0, 17.0, 14.4, 16.8]
Output = [14.99, 15.0]


#Pretty sure I already found a solution for this probelm.
def sub(nums):
  e = sorted(nums.copy())
  d = {}
  for x in range(len(nums)-1):
    if abs(e[0]-e[1]) not in d.keys() and e[0]-e[1]:
      d[abs(e[0]-e[1])] = [e[0], e[1]]
    e.pop(0)
  return [d[min(d)][0], d[min(d)][1]]


#79. Write a Python program to find the largest negative and smallest positive numbers (or 0 if none).
l1 = [-12, -6, 300, -40, 2, 2, 3, 57, -50, -22, 12, 40, 9, 11, 18]
Output = [-6, 2]
l2 = [-1, -2, -3, -4]
Output = [-1, 0]
l3 = [1, 2, 3, 4]
Output= [0, 1]
l4 = []
Output = [0, 0]

#My solution
result = lambda x: [max(sorted(x, reverse=True), key=lambda n: n<0) if len([t for t in x if t<0]) else 0,
                    sorted([s for s in x if s > 0])[0] if len([t for t in x if t>0]) else 0]

#80. Write a Python program to round each float in a given list of number up to the next integer
#and return the running total of the integer squares.

l1 = [2.6, 3.5, 6.7, 2.3, 5.6]
Output = [9, 25, 74, 83, 119]
l2 = [301.1, 401.4, -23.1, 13554122.0, 10201.0101, 10000000.0]
Output = [91204, 252808, 253337, 183714223444221, 183714327525025, 283714327525025]
result = lambda x: [round(x[i-1])**2+round(x[i])**2 if i else round(n)**2 for i, n in enumerate(x)]


result = lambda x: [(int(str(n).split('.')[0])+1)**2 if n > 0 else int(str(n).split('.')[0])**2 for n in x]
added = lambda x : [sum(x[:i]) for i in range(1, len(x)+1)]

#81. Write a Python program to calculate the average of the numbers a through b ( b not included ) rounded 
#to nearest integer, in binary (or -1 if there are no such numbers).

r = range(x, y)



#Stupid udemy puzzle
"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def get_fib(position):
    a = [1]
    while len(a) < position: a += [sum(a[-2:])]
    return a

# Test cases
print get_fib(9)#should get 34
print get_fib(11)#should get 89
print get_fib(0)

#My own: Write a Python program to find the indices of two numbers that sum to 9 in a given list of numbers.
l1 = [7, 1, 5, 6, 4]
l2 = [88, 17, 3, 5, 31, 19, 22, 41, 99, 109, 6, 60, 21, 26, 35, 14, 8]
def result(nums):
    double = nums.copy()
    count = len(nums) - 1
    target = 0
    while target != 9:
        count -= 1
        if count == 1:
            b = double.pop(0)
            double.append(b)
            count = len(nums) - 1
        b = double[0]
        target = 0
        target = double[count] + b
    return [nums.index(double[count]), nums.index(b)]

#Understand the wording of leetcode
'''You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.'''
#ex
# Input:
l1 = [2,4,3], l2 = [5,6,4]
Output = [7,0,8]
# Explanation:
342 + 465 = 807.
# Example 2:
#Input:
l1 = [0], l2 = [0]
Output = [0]
# Example 3:
#Input:
l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output = [8,9,9,9,0,0,0,1]

#solution
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            columnSum = l1Val + l2Val + carry
            carry = columnSum // 10
            newNode = ListNode(columnSum % 10)
            curr.next = newNode
            curr = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummyHead.next
##### Working
class ListNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class Solution:
    def __init__(self):
        self.head = ListNode()
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        now = self.head
        
'''You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.'''

'''Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
'''
#Cool little trick creating a range
#from decimals

# initializing start value
strt = 5
 
# initializing step value
step = 0.4
 
# using list comprehension
# Decimal step range
test_list = [round(strt + (x * step), ndigits=4)
             for x in range(0, 5)]
 
