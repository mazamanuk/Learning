import pytest
from linked_list_cycle import ListNode, Solution

def make_linked_list_with_cycle(values, pos):
    """Helper function to create a linked list with a cycle."""

    nodes = [ListNode(val) for val in values]
    for i in range(len(nodes) -  1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0] if nodes else None

@pytest.mark.parametrize("values, pos, expected", [
    ([3, 2, 0, -4], 1, True), # Given test cases
    ([1, 2], 0, True),
    ([1], -1, False),
    ([1, 2, 3, 4, 5, 6], 0, True),
    ([], -1, False), # Additional test cases
    ([i for i in range(10**4)], 5000, True),
    ([1, 1, 1, 1, 1], -1, False)
])
def test_has_cycle(values, pos, expected):
    head = make_linked_list_with_cycle(values, pos)
    sol = Solution()
    assert sol.hasCycle(head) == expected
