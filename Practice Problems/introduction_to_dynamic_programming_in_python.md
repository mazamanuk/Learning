# Introduction to Dynamic Programming in Python

_Dynamic Programming_ is a programming technique used to solve recursive problems more efficiently.
Let's take a look at a simple algorithm that can get computationally complex very quickly, and then let's use dynamic programming to increase its efficiency.

## Fibonacci

The Fibonacci series is a classic mathematical series in which the next number is calculated as the sum of the previous two numbers:

```
0, 1, 1, 2, 3, 5, 8, 13, 21, etc.
```

The series begins with a `0` and `1`. It can be calculated iteratively by summing the two previous numbers starting with the third entry.
Alternatively, the `n`th Fibonacci number can be calculated recursively.
A recursive solution pseudocode is as follows.

```
function fib(n)
    if n is 1 or 0
        return n
    else
        return fib(n - 1) + fib(n - 2)
```

This technique breaks up calculating the `n`th number into many smaller problems, calculating each step as the sum of calculating the previous two numbers.

Although this technique will certainly work to find the correct number, as `n` grows, the number of recursive calls grows very quickly.
Let's visualize all the function calls if we were to calculate the fourth Fibonacci number:

```
fib(4) -> fib(3) + fib(2)
    fib(3) -> fib(2) + fib(1)
        fib(2) -> fib(1) + fib(0)
    fib(2) -> fib(1) + fib(0)
```

As we ca see fib(2) is called twice, and fib(1) is called three times.
If `n` were larger than 4 we'd see the number of these calls ascend very quickly.
For instance, to calculate the 10th number, we'd make 34 calls to fib(2) and 177 total function calls!
Why do we need to call the same function multiple times with the same input?

We don't!
We can use a technique called _memoization_ to cut down greatly on the number of function calls necessary to calculate the correct number.

## Memoization

_Memoization_ is a specialized form of caching used to store the result of a function call.
The next time that function is called, instead of running the function itself, the result is used directly.
Memoization can result in much faster overall execution times (although it can increase memory requirements as function results are stored in memory).

Memoization is a great technique to use alongside recursion.
The memo can even be saved between function calls if it's being used for common calculations in a program.

### Memoizing Fibonacci

In the previous example, many function calls to fib() were redundant. Let's memoize it in order to speed up execution.

To begin, we'll use a Python dictionary to store the memoized values.
We'll set keys using `n` and values to store the result of that Fibonacci number.
Then, whenever we need to calculate a number, if it's already been calculated, we can retrieve the value from the dictionary in O(1) time.

```python
memo = {}
```

In pseudocode, our approach to memoization will look something like this:

```
Create a memo dictionary

function fibonacci(n):
    if the key, n, exists in memo dictionary
        return memo[n]
    else
        calculate current fibonacci number
        store answer in memo
        return answer
```

Implementation in Python:

Create a memoized `fibonacci()` function.
This function should return the `n`th Fibonacci number.

Note: To avoid an infinite loop, either handle the edge case of negative numbers in your function, or don't call it used negative numbers.

```python
memo = {0: 0, 1: 1}

def fibonacci(num):
    answer = None
    if num < 0:
        return answer
    if num in memo:
        return memo[num]
    answer = fibonacci(num - 1) + fibonacci(num - 2)
    memo[num] = answer
    return answer

# Test your code with calls here:
print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(20))
print(fibonacci(200))
```

Earlier it took 177 function calls to calculate the 10th number. Now, it should only be 19.

## Conclusion

Dynamic programming and memoization are great techniques to break up complex recursive problems into smaller chunks.
They are especially useful when tackling problems that involve combinations.
For example, if I were to ask you to calculate the total number of ways to get four dice to sum to 13, you could imagine breaking that problem into multiple parts.
You could split 13 into 6 and 7 and then find all the combinations of two rolls that would match each one of these.
As you go down each path, you would probably start seeing a lot of similar calculations, and memoization would help you reduce the number of overall function calls by storing intermediate values.

Some other common problems that can be solved using dynamic programming are the knapsack problem, the coin change problem, and the partition problem.
