
<table rules=none>
 <tr>
<td> <img src="https://i.imgur.com/GjPtRPW.png"></td>
<td> <h2><a href="https://joshjetson.github.io">Python Puzzles</a></h2><br>An assortment of Python Puzzles to help make you think like a programmer</td>
</tr>
</table>


> This page is intended to give python programmers some alternative ways of looking at solving problems.


## List Processing

------------------------

**Find the singular item in a list**

*Example List*

```python
num_list = [1, 1, 3, 4, 7, 3, 7]
```


*Solution*


> A long solution

```python
num_list.sort()
count = []
singular = 0
check_list = []
for num in num_list:
	count.append(1)
	if len(count) == len(num_list):
		print(f'The only unique number in the list is: {singular}')
	elif num_list.count(num) < 2:
		singular += num
	elif num_list.count(num) >= 2:
		if num not in check_list:
			check_list.append(num)
			print(f 'The number {num}, is a duplicate')
```

> A solution using list comprehension

```python
nums_count = [f'singular digit =  {x}' for x in num_list if num_list.count(x) == 1]
```

> A solution using lambda

```python
result = lambda x: list(filter(lambda y: (x.count(y) == 1), x))
result(num_list)
```




**Count the even, odd numbers in a given array of integers using Lambda.**

```python
nums = [1, 2, 3, 5, 7, 8, 9, 10]

# Quick soulution using the filter method.
odd_ctr = len(list(filter(lambda x: (x%2 != 0), nums)))
even_ctr = len(list(filter(lambda x: (x%2 == 0), nums)))


#or combined in a gnarly solution
result = lambda x: ('{0} EVEN NUMBERS'.format(len(list(filter(lambda y: (y%2 == 0),x)))), '{0} ODD NUMBERS'.format(len(list(filter(lambda y: (y%2 == 1),x)))))

```



**Find the element in a list that is length 6**

```python
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Using filter
days = filter(lambda day: day if len(day)==6 else '', weekdays)

# Using list comprehension
day_lst = [day for day in days if len(day)==6]
# A more dynamic solution
result = lambda x, y: list(filter(lambda z: (len(z) == y), x))
result(weekdays, 6)# = ['Monday', 'Friday', 'Sunday']

```


**Add two given lists using map and lambda**

```python
num1 = [1,2,3]
num2 = [4,5,6]
# A Solution
combine = list(map(lambda a, b: a + b, num1, num2))
# This can simplify to the below using list comprehension
combine = [*map(lambda a, b: a + b, num1, num2)]
```


## Fun With Functions

-------------------------------

**Write a program that receives user input which defines N number of students along with their names and grades and then finds the second lowest grade among them all**



```python
def grade_calc(loop=None, students=None, grades=[]):
  num = input(f'How many students are there ? ') if not loop else None
  if not loop and not num.isnumeric(): return grade_calc()
  loop = num



```
