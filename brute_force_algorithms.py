## Creating linear search algorithms implementing a brute force approach to searching a given input list
# Setting up a list to search through and a target value to search for
number_list = [ 10, 14, 19, 26, 27, 31, 33, 35, 42, 44]
target_number = 33
# Linear search function loops through all input indices searching for the target value, if target is found we return the index within the list
# otherwise we raise a value error with a message indicating that the target is not within our search list
def linear_search(search_list, target_value):
    for idx in range(len(search_list)):
        if search_list[idx] == target_value:
            return idx
    raise ValueError("{0} not in list".format(target_value))

result = linear_search(number_list, 33)
print(result)
# Output here will be:
'''
6
'''

try:
    result = linear_search(number_list, 100)
    print(result)
except ValueError as error_message:
    print("{0}".format(error_message))
# Output here will be:
'''
100 not in list
'''

# Setting up a search list looking for multiple occurrences of a target value
tour_locations = [ "New York City", "Los Angeles", "Bangkok", "Istanbul", "London", "New York City", "Toronto"]
target_city = "New York City"

# Search function here iterates through all indices of the search list, if the target value is found we append the index to an output list
# If the output list is empty at the end of the function, raise a value error, otherwise return the list containing value indices
def linear_search(search_list, target_value):
    matches = []
    for idx in range(len(search_list)):
        if search_list[idx] == target_value:
            matches.append(idx)
    if len(matches) == 0:
        raise ValueError("{0} not in list".format(target_value))
    return matches

tour_stops = linear_search(tour_locations, target_city)
print(tour_stops)
# Output here will be:
'''
[0, 5]
'''

test_scores = [88, 93, 75, 100, 80, 67, 71, 92, 90, 83]

# Search function iterates through all indices and compares a maximum score index to the value at the iterated index, if the value is larger
# than the value at the current maximum score index, we replace the value and return the maximum scxore index at the end
def linear_search(search_list):
    maximum_score_index = None
    for idx in range(len(search_list)):
        print(search_list[idx])
        if maximum_score_index is None or search_list[idx] > search_list[maximum_score_index]:
            maximum_score_index = idx
    return maximum_score_index

highest_score = linear_search(test_scores)
print(highest_score)
# Output here will be:
'''
88
93
75
100
80
67
71
92
90
83
3
'''