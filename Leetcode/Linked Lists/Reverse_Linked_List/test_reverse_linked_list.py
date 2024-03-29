import pytest
from reverse_linked_list import ListNode, Solution
from typing import Optional

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

@pytest.mark.parametrize("values, expected", [
    ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]), # Given test cases
    ([1, 2], [2, 1]),
    ([], []), # Additional test cases
    ([i for i in range(5000)], [i for i in range(5000)][::-1])
])
def test_reverse_list(values, expected):
    head = make_linked_list(values)
    sol = Solution()
    reversed_head = sol.reverseList(head)
    assert linked_list_to_list(reversed_head) == expected
