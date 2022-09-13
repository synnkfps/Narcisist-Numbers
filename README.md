## Narcisist-Numbers
algorithm to find narcisist numbers in Python!

### Narcisist Numbers Logic
Get a number, for example 1634, get its digits and sum them by its power of the length of the number

1634: 1^4 + 6^4 + 3^4 + 4^4 = 1634 <br>
153: 1^3 + 5^3 + 3^3 = 153

### Algorithm Logic
Add to a variable all the numbers of a number on the power of its length

Python Algorithm:
```py
number = 1634
result = 0

for x in str(number):
    result += int(x)**len(str(number))
```

My code uses the algorithm but it finds the current number in a range of value.
So in range 100 to 13000, we have the following narcisist numbers:
```
153
370
371
407
1634
8208
9474
```
