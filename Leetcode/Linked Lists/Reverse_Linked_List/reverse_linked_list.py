from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Keeping track of two nodes at a time, we reassign next pointers until we reach the end of the list
        prev, curr = None, head
        # Run while we have a 'current' node
        while curr:
            # Set a temporary variable equal to the next node in the list
            nxt = curr.next
            # Set our current node's next pointer to the current 'previous' node to begin reversing the list
            curr.next = prev
            # Complete the shifting of pointers along the list to continue the loop
            prev = curr
            curr = nxt
        # Finally, return the 'previous' node which is set to the original tail of the list
        return prev
