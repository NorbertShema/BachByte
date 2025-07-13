# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]

        Understand
            -input: linked list 
            -output: middle node
            -Constraints: The list is non-empty and then node values are positive integers
            =Edge cases:-Even number of nodes, return the second mid. 
                        - Odd number of nodes, return the middle node.

        plan:
            - Use fast and slow pointer: This will work because the fast pointer moves twice as fast as the slow pointer.
             so when the fast gets at the end of the linked list, the slow will be exactly pointing at the middle node.

        Implement
            
        """
        fast = head                     ##initialize the pointers
        slow = head

        while fast and fast.next:
            fast = fast.next.next       ## fast moves two times
            slow = slow.next            ## slow moves once

        return slow        