
<table rules=none>
 <tr>
<td> <img src="https://i.imgur.com/GjPtRPW.png"></td>
<td> <h2><a href="https://joshjetson.github.io">Python Puzzles</a></h2><br>An assortment of Python Puzzles to help make you think like a programmer</td>
</tr>
</table>


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
		print('The only unique number in the list is: %d' %(singular))
	elif num_list.count(num) < 2:
		singular += num
	elif num_list.count(num) >= 2:
		if num not in check_list:
			check_list.append(num)
			print('The number %d' %(num), 'is a duplicate')
```

> A solution using list comprehension

```python
nums_count = ['singular digit =  {0}'.format(x) for x in num_list if num_list.count(x) == 1]
```

> A solution using lambda

```python
result = lambda x: list(filter(lambda y: (x.count(y) == 1), x))
result(num_list)
```

-------------------------------
