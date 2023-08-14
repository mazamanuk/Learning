# Sieve of Eratosthenes

The _Sieve of eratosthenes_ is one of the oldest-known algorithms, and it's still helpful for deriving primt numbers!
The algorithm is attributed to Eratosthenes, a Greek mathematician born in the third century BCE.

The sieve provides a set of steps for finding all primes up to a given limit.
As a reminder, a prime number is a positive number with no divisors but `1` and itself.
`2`, `3`, `11` and `443` are all prime numbers.

## Sieve Implementation

The sieve works by first assuming that all numbers from

```
{2, ..., n}
```

are prime, and then successfully marking them as NOT prime.

The algorithm works as follows:

1. Create a list of all integers from 2 to n.
2. Start with the smallest number in the list (2, the smallest prime number).
3. Mark all multiples of that number up to n as not prime.
4. Move to the next non-marked number and repeat this process until the entire list has been covered.

When the steps are complete, all remaining non-marked numbers are prime.

### Example

If we wanted to find all prime numbers less than or equal to 10, we would:

1.  Start with a list where all are assumed to be prime:

    2 3 4 5 6 7 8 9 10

2.  Starting with `2`, mark all multiples up to `10` as NOT prime:

    2 3 ~~4~~ 5 ~~6~~ 7 ~~8~~ 9 ~~10~~

3.  Move to the next non-marked number, `3`, and mark its multiples as NOT prime (`6`) is already marked:

    2 3 ~~4~~ 5 ~~6~~ 7 ~~8~~ ~~9~~ ~~10~~

4.  Continue marking, starting with ever non-marked number (in this case, all multiples of `5` are already marked, and `7`'s first multiple is out of range).
    This means that we have now found all primes up to `10`:

    2 3 ~~4~~ 5 ~~6~~ 7 ~~8~~ ~~9~~ ~~10~~

## Implementation Steps in Python

There are many possible ways of implementing this algorithm in Python.
We'll outline a basic approach here and then walk through it step-by-step.

1. Create an array of all integers from `2` to `n`.
2. Set all elements of the array to `True`.
3. Starting with `2`, iterate through the array. If the current element is `True`, it is still considered prime. Since we know that all multiples of that number are NOT prime, iterate through all multiples of that number up to `n` and set them equal to `False`.
4. Change the current element to the next non-`False` index.
5. Return the corresponding number value for any element still marked as prime (value of `True`).

### Step One: Create the Array

First, we'll create the array.
In this case, we'll create an array to represent all numbers up top the input limit, but we'll use the array index to represent the number, and it's value (`True/False`) to represent whether it is prime or not.
The original algorithm said to use an array of `2, ..., n` but since we're using indices to represent the actual number we'll start the array from `0` and essentially ignore the values of `array[0]` and `array[1]`.

For example, after running our sieve, an array representing the primes up to `7` would look like this, with elements at `[2]`, `[3]`, `[5]` and `[7]` marked `True`:

```python
[False, False, True, True, False, True, False, True]
```

Implementation in Python:

```python
def sieve_of_eratosthenes(limit):
    output = [True] * (limit + 1)
    output[0] = False
    output[1] = False
```

### Step Two: Iterate

Now we'll implement the bulk of the algorithm to iterate and mark numbers as non-prime.
We'll do this in two steps:

1. Create an outer loop to iterate from `2` to the limit.
2. Inside, check if the current number is still marked prime. If it is, we'll mark all its multiples using another loop.

Implementation in Python:

```python
def sieve_of_eratosthenes(limit):
    output = [True] * (limit + 1)
    output[0] = False
    output[1] = False

    for i in range(2, limit + 1):
        if (output[i] == True):
            j = i*2
            while j <= limit:
                output[j] = False
                j = j + i
```

### Step Three: Return Values

Now it's time to pare down our array and only return the actual primes.
One way to do this is:

- Create an enumerate object of tuples (index, values) using the `enumerate()` function where index is an incremental number beginning with `0` and value is a boolean value of either `True` or `False`.
- Convert the enumerate object to a list with the `list()` function.
- Use list comprehension to create only a list of indices whose corresponding values are `True`.
- Return a list of indices.

Implementation in Python:

```python
def find_true_indices(inputs):
  true_indices = [index for (index, value) in list(enumerate(inputs)) if value == True]
  return true_indices

test = find_true_indices([False, False, True, True, False, True, False, True])

print(test); # should return [2, 3, 5, 7]
```

## Complete Algorithm

```python
def sieve_of_eratosthenes(limit):
    true_indices = []

    # Handle edge cases
    if (limit <= 1):
        return true_indices

    # Create output list
    output = [True] * (limit + 1)

    # Mark 0 and 1 as non-prime
    output[0], output[1] = False, False

    # Iterate through the list
    for i in range(2, limit + 1):
        if output[i] == True:
            j = i * 2
            # Mark all multiples of i as non-prime
            while j <= limit:
                output[j] = False
                j += i

    # Remove non-prime numbers
    true_indices = [index for (index, value) in list(enumerate(output)) if value == True]

    return true_indices

primes = sieve_of_eratosthenes(13)
print(primes) # should return [2, 3, 5, 7, 11, 13]
```

### Optimizations

There are several small optimizations that can be made to the basic implementation of the sieve to remove duplicate for prime-ness.

#### End Boundary

In our basic implementation, the outer loop iterated from `2` to `n`.
Because the inner loop marks multiples of a base value, we only need to check individual numbers lower than the square root of `n`.
Consider the example of a limit of `10`:

1. First, all multiples of `2` are marked:

   2 3 ~~4~~ 5 ~~6~~ 7 ~~8~~ 9 ~~10~~

2. Then all multiples of `3` are marked:

   2 3 ~~4~~ 5 ~~6~~ 7 ~~8~~ ~~9~~ ~~10~~

3. `4` is greater than the square root of `10` (approximately `3.16`), so we can break. If you look at the previous step, all non-prime numbers have indeed already been marked.

#### First Multiple

In our basic implementation, the inner loop started checking multiples at 2 times the current number.
We can skip a few checks starting the checks at current<sup>2</sup>.

Consider the example of a limit of `10` again:

1.  First, all multiples of `2` are marked:

    2 3 ~~4~~ 5 ~~6~~ 7 ~~8~~ 9 ~~10~~

2.  Then, all multiples of `3` are marked, but we can skip `6` (`3` \* `2`) because it's already been marked.
    Instead we start at 3<sup>2</sup>, `9`:

    2 3 ~~4~~ 5 ~~6~~ 7 ~~8~~ ~~9~~ ~~10~~

3.  We've now completed the check with one less comparison.

#### Pre-mark All Even Numbers

This optimization comes in when building the initial array. There's no need to ever check even numbers after `2`, since they will never be prime, so they can all be marked as non-prime initially.

---

These optimizations may seem small when dealing with a limit of `10`, but they can significantly speed up the algorithm with larger limits.

## Complexity

The complexity of the Sieve of Eratosthenes with optimization is

    O(n log (log n))

There are two operations to take into account: the creation of the array and the incrementing and multiple-marking loops.

Creation happens in `O(n)` time, since it creates an element for each number from 2 to `n`.

Multiple marking happens in `O(n log (log n))` time.
The reasons for this come down to some complex maths, but briefly:

The number of times you mark a non-prime number is

$\frac{n}{2}$ + $\frac{n}{3}$ + ...$\frac{n}{\sqrt{n}}$

It begins with `n / 2` because initially all multiples of `2`are marked as non-prime (this will happen 50 times with a limit of 100, as each even number is marked).
This process continues up until the square root of `n`.
Through some [fancy mathematical proof](https://en.wikipedia.org/wiki/Divergence_of_the_sum_of_the_reciprocals_of_the_primes), this works out to an overall time complexity of

    O(n log (log n))

since this is larger than the `O(n)` array-creation time.

## Conclusion

The Sieve of Eratosthenes is a millenia-old algorithm, so there are some more improvements and more advanced methods for finding primes invented since its discovery, but it's still a great way to generate lists of prime numbers.
Included below is our sieve code including optimizations:

```python
# import math library
import math

def sieve_of_eratosthenes(limit):
    # Handle edge cases
    if (limit <= 1):
        return []

    # Create the output list
    output = [True] * (limit + 1)

    # Mark 0 and 1 as non-prime
    output[0], output[1] = False, False

    # Iterate up to the square root of the list
    for i in range(2, math.floor(math.sqrt(limit))):
        if (output[i] == True):
            j = i ** 2 # Initialize j to square of i

            # Mark all multiples of i as non-prime
            while j <= limit:
                output[j] = False
                j += i

    # Remove non-prime numbers
    output_with_indices = list(enumerate(output))
    trues = [index for (index, value) in output_with_indices if value ==  True]
    return trues

primes = sieve_of_eratosthenes(20)
print(primes) # return [2, 3, 5, 7, 11, 13, 17, 19]
```
