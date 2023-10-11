from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: Optional[ListNode] = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Keeping pointers at a 'slow' and 'fast' node to compare later
        curr_slow = head
        curr_fast = head
        # Run as long as the fast node and its next node aren't None
        while curr_fast and curr_fast.next:
            # Set slow node to its next node
            curr_slow = curr_slow.next # type: ignore
            # Set fast node to its next next node
            curr_fast = curr_fast.next.next
            # If the two nodes are ever equal again, return True as we have a cycle
            if curr_slow == curr_fast:
                return True
        # Return False if we end the loop and we haven't found a cycle
        return False
