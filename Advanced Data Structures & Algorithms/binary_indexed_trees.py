## Range of Responsibility

arr = [1, 8, 7, 2, 5, 11, 4, 16, 7, 17, 9, 6, 12, 15, 27, 19, 22, 21, 3, 20] 

def range_of_responsibility(number):
    range_of_responsibility = 0
    binary_rep = bin(number)[2:]
    for digit in range(len(binary_rep))[::-1]:
        if binary_rep[digit] == "1":
            r = len(binary_rep) - digit - 1
            range_of_responsibility = 2**r
            break
    return range_of_responsibility

print(range_of_responsibility(12))

def array_value(arr, number):
    value = 0
    range_of_res = range_of_responsibility(number)
    for index in range(number - range_of_res, number):
        value += arr[index]
    return value

print(array_value(arr, 12))
print(array_value(arr, 15))

element12 = 39
element15 = 27