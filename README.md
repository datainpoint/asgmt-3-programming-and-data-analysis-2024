# asgmt-3-programming-and-data-analysis-2024

> Assignment 3: Programming and Data Analysis 2024.

- Define functions in `asgmt.py` given their names, templates, and docstrings.
- Run `test-runner.py` to validate your functions.
- Upload `asgmt.py` to [NTU COOL](https://cool.ntu.edu.tw).

## 01. Define a function `return_shape_name()` which returns the shape name given number of corners.

```python
def return_shape_name(number_of_corners: int) -> str:
    """
    >>> return_shape_name(0)
    'Circle'
    >>> return_shape_name(3)
    'Triangle'
    >>> return_shape_name(4)
    'Rectangle'
    >>> return_shape_name(5)
    'Pentagon'
    >>> return_shape_name(6)
    'Hexagon'
    """
    ### BEGIN SOLUTION

    ### END SOLUTION
```

## 02. Define a function `count_of_positives()` which returns the number of positive integers given a `list`.

```python
def count_of_positives(x: list) -> int:
    """
    >>> count_of_positives([0, 1, 2, 3])
    3
    >>> count_of_positives([-3, -2, -1, 0, 1, 2, 3])
    3
    >>> count_of_positives([0, 1, 2, 3, 4, 5])
    5
    >>> count_of_positives([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])
    5
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 03. Define a function `sum_of_negatives()` which returns the summation of negative integers given a `list`.

```python
def sum_of_negatives(x: list) -> int:
    """
    >>> sum_of_negatives([-3, -2, -1, 0])
    -6
    >>> sum_of_negatives([-3, -2, -1, 0, 1, 2, 3])
    -6
    >>> sum_of_negatives([-5, -4, -3, -2, -1, 0])
    -15
    >>> sum_of_negatives([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])
    -15
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 04. Define a function `return_with_fizz_buzz_rule()` which returns a given integer with Fizz Buzz rule.

Source: <https://en.wikipedia.org/wiki/Fizz_buzz>

```python
def return_with_fizz_buzz_rule(x: int):
    """
    >>> return_with_fizz_buzz_rule(3)
    'Fizz'
    >>> return_with_fizz_buzz_rule(5)
    'Buzz'
    >>> return_with_fizz_buzz_rule(15)
    'Fizz Buzz'
    >>> return_with_fizz_buzz_rule(16)
    16
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 05. Define a function `return_first_n_fizz_buzz()` which returns the first `n` Fizz Buzz integer/string as a `list`.

```python
def return_first_n_fizz_buzz(n: int) -> list:
    """
    >>> return_first_n_fizz_buzz(4)
    [1, 2, 'Fizz', 4]
    >>> return_first_n_fizz_buzz(6)
    [1, 2, 'Fizz', 4, 'Buzz', 'Fizz']
    >>> return_first_n_fizz_buzz(15)
    [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'Fizz Buzz']
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 06. Define a function `range_fizz_buzz()` which returns a list of Fizz Buzz integer/string given `start`(inclusive) and `stop`(exclusive).

```python
def range_fizz_buzz(start: int, stop: int) -> list:
    """
    >>> range_fizz_buzz(1, 5)
    [1, 2, 'Fizz', 4]
    >>> range_fizz_buzz(3, 5)
    ['Fizz', 4]
    >>> range_fizz_buzz(1, 6)
    [1, 2, 'Fizz', 4, 'Buzz']
    >>> range_fizz_buzz(3, 6)
    ['Fizz', 4, 'Buzz']
    >>> range_fizz_buzz(1, 16)
    [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'Fizz Buzz']
    >>> range_fizz_buzz(13, 16)
    [13, 14, 'Fizz Buzz']
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 07. Define a function `retrieve_middle_elements()` which returns the middle elements of a given list. If there are two middle elements, return both of them in a tuple.

```python
def retrieve_middle_elements(x: list):
    """
    >>> retrieve_middle_elements([2, 3, 5])
    3
    >>> retrieve_middle_elements([2, 3, 5, 7])
    (3, 5)
    >>> retrieve_middle_elements([2, 3, 5, 7, 11])
    5
    >>> retrieve_middle_elements([2, 3, 5, 7, 11, 13])
    (5, 7)
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 08. Define a function `median()` which returns the median value of a given unsorted list. The median value can be calculated as the average of middle elements after sorting the given list in ascending order.

Source: <https://en.wikipedia.org/wiki/Median>

```python
def median(x: list):
    """
    >>> median([2, 3, 5, 7, 11])
    5
    >>> median([2, 3, 5, 7, 11, 13])
    6.0
    >>> median([11, 13, 17, 2, 3, 5, 7])
    7
    >>> median([7, 11, 13, 17, 19, 2, 3, 5])
    9.0
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 09. Define a function `collect_divisors()` which returns all positive divisors of a given integer.

Source: <https://en.wikipedia.org/wiki/Divisor>

```python
def collect_divisors(x: int) -> list:
    """
    >>> collect_divisors(1)
    [1]
    >>> collect_divisors(2)
    [1, 2]
    >>> collect_divisors(3)
    [1, 3]
    >>> collect_divisors(4)
    [1, 2, 4]
    >>> collect_divisors(5)
    [1, 5]
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 10. Define a function `is_prime()` which returns whether `x` is a prime number or not.

Source: <https://en.wikipedia.org/wiki/Prime_number>

```python
def is_prime(x: int) -> bool:
    """
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(5)
    True
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```