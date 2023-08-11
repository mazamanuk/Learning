# The Knapsack Problem

Recursive and dynamic programming approaches to the classic knapsack problem in Python.

Imagine that you're a thief breaking into a house. There are so many valuables to steal - diamonds, gold, jewellery, and more! But remember, you're just one person who can only carry so much. Each item has a weight and value, and your goal is to maximize the total value of items while remaining within the weight limit of your knapsack. This is called the knapsack problem and is commonly used in programming interviews. We will solve this problem in two ways: recursively, and using dynamic programming.

### The Problem

The first step to solving this problem is to understand the parameters involved.

You will be given:

- the total amount of weight you can carry (`weight_cap`)
- the weights if all if the items in an array (`weights`)
- the values of all of the items in an array (`values`)

Your function should return the maximum value that you will be able to carry.

#### An Example

Let's say that you have a knapsack that can only carry 5 pounds, and the house you're robbing has three items that you want to steal:

1. A ring that weighs 1 pound with a value of $250
2. Earrings that weigh 3 pounds with a value of $300
3. A necklace that weighs 5 pounds with a value of $500

This information can be summarized as follows:

```
weight_cap = 5
weights = [1, 3, 5]
values = [250, 300, 500]
```

You have four possible ways to fill your knapsack:

1. Take only the ring, giving you $250
2. Take only the earrings, giving you $300
3. Take only the necklace, giving you $500
4. Take the ring and the earrings, giving you $550

Since the ring and the earrings have a combined weight of 4 pounds, taking both gives you the maximum value while staying within your weight capacity. Now that you're familiar with the problem, let's take a look at two different approaches to solving it!

### The Recursive Solution

The brute force solution to this problem is to look at every subset of the items that has a total weight less than `weight_cap`. Then you simple take the maximum of those subsets, giving you the optimized subset with the highest value possible.

You will need an additional parameter, `i`, that tells us where we are in the list of items. With each step, we will break the problem down into subproblems, and compare them to find the maximum value. There are three possibilities for every call of the function:

1. `weight_cap` or `i` are zero, meaning the knapsack can hold no weight, or there are no more items to look at. In either case, we return `0`.
2. The weight of the item we're looking at exceeds `weight_cap`, in which case we just move on, calling the function on the next item.
3. If neither of the above are true, that means we have to consider whether or not the item we are at (`i`) should be included in the optimal solution.

Steps 1 and 2 from above can be solved as follows:

```python
def recursive_knapsack(weight_cap, weights, values, i):
    # base condition
    if weight_cap == 0 or i == 0:
        return 0
    # recursive solution
    elif weights[i - 1] > weight_cap:
        return recursive knapsack(weight_cap, weights, values, i - 1)
```

For step 3, we need to look at both situations and determine if we want to include this item in our optimized solution or not.

```python
def recursive_knapsack(weight_cap, weights, values, i):
    if weight_cap == 0 or i == 0:
        return 0
    elif weights[i - 1] > weight_cap:
        return recursive_knapsack(weight_cap, weights, values, i - 1)
    else:
        include_item = values[i - 1] + recursive_knapsack(weight_cap - weights[i - 1], weights, values, i - 1)
        exclude_item = recursive_knapsack(weight_cap, weights, values, i - 1)
        return max(include_item, exclude_item)
```

While this recursive solution works, it has a big O runtime of O(2<sup>n</sup>). In the worst case, each step would require us to evaluate two subproblems, sometimes repeatedly, as there's overlap between subproblems. We can drastically improve on this runtime by using dynamic programming.

### The Dynamic Programming Approach

The knapsack problem is suited for dynamic programming because memoization will allow us to store information instead of making duplicate calls. We will store this information in a two-dimensional array that has a row for every item and `weight_cap + 1` number of columns where each element in the 2D array (`matrix`) represents a subproblem. The element at the bottom right will be the optimal solution.

But what exactly do the rows and columns represent? The rows represent the items we have seen. So if we are at row `4`, then we have only seen the first `4` items, meaning the others aren't being considered yet. The columns represent how much weight the knapsack can hold. If we are at column 7, then we are looking at a subset of the larger problem where our knapsack has a weight capacity of `7`. The number stored inside `matrix` is the maximum value we can take given the weight capacity and number of items we have seen for that subproblem. By the time we get to the bottom right space in `matrix`, we have considered every possible subproblem and taken the maximum possible value.

There are some elements in the matrix that will be easy to fill. Every element in the zeroth row represents a subproblem with 0 items to consider, so there is no value. Likewise every element in the zeroth column represents a subproblem where our knapsack has a capacity of 0, giving us no value to take. Because of this we start by filling the zeroth row and column with `0`.

The pseudocode for the entire algorithm is as follows:

```
matrix = 2D array with rows equal to number of items and empty columns
for every number of items you can carry (index):
    fill matrix[index] with an array of length weight_cap + 1
    for every weight < weight_cap (weight):
        if index or weight == 0:
            set element at [index][weight] to 0
        else if the weight of the element at index - 1 <= weight:
            find possible values of including and excluding the item
            set element at [index][weight] to max of those values
        else:
            set element at [index][weight] to element one above
return element at bottom right of matrix
```

Implementation in Python:

```python
def dynamic_knapsack(weight_cap, weights, values):
    rows = len(weights) + 1
    cols = weight_cap + 1
    # Set up 2D array
    matrix = [ [] for x in range(rows) ]

    # Iterate through every row
    for index in range(rows):
        # Initialize columns for this row
        matrix[index] = [ -1 for y in range(cols) ]

        # Iterate through every column
        for weight in range(cols):
            # Write your code here
            if index == 0 or weight == 0:
                matrix[index][weight] = 0
            # If weight at previous row is less than or equal to the current weight
            elif weights[index - 1] <= weight:
                # Calculate item to include
                include_element = weights[index - 1] + matrix[index - 1][weight - weights[index - 1]]
                # Calculate item to exclude
                exclude_element = matrix[index - 1][weight]
                # Calculate the value of the current cell
                matrix[index][weight] = max(include_element, exclude element)
            else:
                # Calculate the value of the current cell
                matrix[index - 1][weight]
    # Return the value of the bottom right of matrix
    return matrix[rows - 1][weight_cap]

# Use this to test your function:
weight_cap = 50
weights = [31, 10, 20, 19, 4, 3, 6]
values = [70, 20, 39, 37, 7, 5, 10]
print(dynamic_knapsack(weight_cap, weights, value))
```

This version has a big O runtime of O(n \* weight_cap), compared to the recursive implementation's runtime of O(2<sup>n</sup>). While this optimized runtime might seem worse using small cases, it is much more efficient as the parameters grow.
