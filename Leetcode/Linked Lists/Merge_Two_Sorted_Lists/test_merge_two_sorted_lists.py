import pytest
from typing import Optional
from merge_two_sorted_lists import ListNode, Solution

def make_linked_list(values):
    """Helper function to create a linked list."""

    nodes = [ListNode(val) for val in values]
    for i in range(len(nodes) -  1):
        nodes[i].next = nodes[i + 1]
    return nodes[0] if nodes else None

def linked_list_to_list(node: Optional[ListNode]):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

@pytest.mark.parametrize("list1, list2, expected", [
    ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]), # Given test cases
    ([], [], []),
    ([], [0], [0]),
    ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]), # Additional test cases
    ([2, 3], [1], [1, 2, 3]),
])
def test_merge_two_lists(list1, list2, expected):
    linked_list_1 = make_linked_list(list1)
    linked_list_2 = make_linked_list(list2)
    
    sol = Solution()
    merged_head = sol.mergeTwoLists(linked_list_1, linked_list_2)
    
    assert linked_list_to_list(merged_head) == expected