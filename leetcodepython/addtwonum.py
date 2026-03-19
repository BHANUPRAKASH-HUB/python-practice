# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)  # Dummy node to simplify the head of the return list
        current = dummy      # Pointer to build the new linked list
        carry = 0            # Keep track of the carry-over value

        # Loop until both lists are exhausted AND there is no carry left
        while l1 or l2 or carry:
            # Get the values from the current nodes (use 0 if a list is exhausted)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate the total sum for this digit column
            total = val1 + val2 + carry
            
            # Update carry for the next column (e.g., 14 // 10 = 1)
            carry = total // 10
            
            # Create a new node with the digit part of the sum (e.g., 14 % 10 = 4)
            current.next = ListNode(total % 10)

            # Move the pointers forward
            current = current.next
            if l1: 
                l1 = l1.next
            if l2: 
                l2 = l2.next

        # The actual result skips our initial dummy node
        return dummy.next
