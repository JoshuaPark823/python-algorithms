"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        # Set the current position to the head
        current = head

        # Because we're at the head, the previous node dne
        previous =None
        next = None
        
        # Iterate while the current node isn't null
        while current:

            # Set next as the current node's next pointer
            next= current.next

            # Set the current's next pointer to point to the previous node (going backwards)
            current.next =previous

            # Set the previous node as the current node
            previous = current

            # Set the current node to the next node
            current = next

        # Return the new head
        return previous
