from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # We define a ListNode to store the nodes from each list in order
        curr = output = ListNode()
        # While nodes exist in both lists
        while list1 and list2:
            # If the node at list1 is less than the node at list2, we set the current node's next pointer to list1's node and increment both curr and list1
            if list1.val < list2.val:
                curr.next = list1
                list1, curr = list1.next, list1
            # Otherwise, we set the current node's next pointer to list2's node and increment both curr and list2
            else:
                curr.next = list2
                list2, curr = list2.next, list2
        # If one of the lists is empty and the other contains remaining nodes
        if list1 or list2:
            # Set our remaining nodes in order as our current node's next pointer
            curr.next = list1 if list1 else list2
        # Finally, return the output we defined earlier with all nodes in order
        return output.next
