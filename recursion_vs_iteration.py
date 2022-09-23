## Factorial function using iterative method
# O(N)
def factorial(n):  
    if n < 0:    
        ValueError("Inputs 0 or greater only") 
    if n <= 1:    
        return 1  
    return n * factorial(n - 1)

## Factorial function using recursive method
def factorial(n):
    num = 1
    for i in range(n):
        num *= i+1
    return num


## Fibonacci function using iterative method
# O(2^N)
def fibonacci(n):
    fibs = [1 for i in range(n+1)]
    fibs[0] = 0
    for i in range(2,n+1):
        fibs[i] = fibs[i-1] + fibs[i-2]
    return fibs[n]
## Alternate iterative method
def fibonacci(n):
    fibs = [0, 1]
    if n <= len(fibs)-1:
        return fibs[n]
    else:
        while n > len(fibs)-1:
            fibs.append(fibs[-1]+fibs[-2])
        return fibs[n]

## Fibonacci function using recursive method
def fibonacci(n):
    if n < 0:
        ValueError("Input 0 or greater only!")
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


## Sum digits function using iterative method
# O(N) (where N is the number of digits in the number)
def sum_digits(n):
    if n < 0:
        ValueError("Input 0 or greater only!")
    result = 0
    while n is not 0:
        result += n % 10
        n = n // 10
    return result + n

## Sum digits function using recursive method
def sum_digits(n):
    if n < 0:
        ValueError("Input 0 or greater only!")
    result = 0
    if n < 10:
        return n
    last_digit = n % 10
    return last_digit + sum_digits(n // 10)


## Find min function using iterative method
# O(N)
def find_min(my_list):
    min = None
    for element in my_list:
        if not min or (element < min):
            min = element
    return min

## Find min function using recursive method
def find_min(my_list, min=None):
    if len(my_list) == 0:
        return min
    else:
        if min is None or my_list[0] < min:
            min = my_list[0]
    return find_min(my_list[1:], min)


## Is palindrome function using iterative method
# O(N^2)
def is_palindrome(my_string):
    while len(my_string) > 1:
        if my_string[0] != my_string[-1]:
            return False
        my_string = my_string[1:-1]
    return True

## More efficient version using iterative method
# O(N)
def is_palindrome(my_string):
    string_length = len(my_string)
    middle_index = string_length // 2
    for index in range(0, middle_index):
        opposite_character_index = string_length - index - 1
        if my_string[index] != my_string[opposite_character_index]:
            return False  
    return True

## Is palindrome function using recursive method
def is_palindrome(my_string):
    if len(my_string) < 2:
        return True
    if my_string[0] != my_string[-1]:
        return False
    return is_palindrome(my_string[1:-1])


## Multiplication function using iterative method
# O(N)
def multiplication(num_1, num_2):
    result = 0
    for count in range(0, num_2):
        result += num_1
    return result

## Multiplication function using recursive method
def multiplication(num_1, num_2):
    if num_1 == 0 or num_2 == 0:
        return 0
    return num_2 + multiplication(num_1 - 1, num_2)


## Depth of a tree function using iterative method
# O(N)
def depth(tree):
    result = 0
    queue = [tree]
    while queue:
        level_count = len(queue)
        for child_count in range(0, level_count):
            child = queue.pop(0)
            if child["left_child"]:
                queue.append(child["left_child"])
            if child["right_child"]:
                queue.append(child["right_child"])
        result += 1
    return result

## Depth of a tree function using recursive method
def depth(tree):
    if tree is None:
        return 0
    if not tree["left_child"] and not tree["right_child"]:
        return 1
    count = 1
    return count + depth(tree["left_child"])

## Alternate recursive method
def depth(tree):
    if tree is None:
        return 0
    left_depth = depth(tree["left_child"])
    right_depth = depth(tree["right_child"])
    if left_depth > right_depth:
        return left_depth + 1
    return right_depth + 1

## Binary Search Tree builder implementation for use with depth functions above
def build_bst(my_list):
    if len(my_list) == 0:
        return None
    mid_idx = len(my_list) // 2
    mid_val = my_list[mid_idx]
    tree_node = {"data": mid_val}
    tree_node["left_child"] = build_bst(my_list[ : mid_idx])
    tree_node["right_child"] = build_bst(my_list[mid_idx + 1 : ])
    return tree_node