from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: Optional[ListNode] = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr_slow = head
        curr_fast = head
        while curr_fast and curr_fast.next:
            curr_slow = curr_slow.next # type: ignore
            curr_fast = curr_fast.next.next
            if curr_slow == curr_fast:
                return True
        return False
