# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]

        Hint:
            -The prev pointer is going to be the new head after the linked listed has been reversed.
        
            - follow the order( initialize pointer, flip them to reversed and keep moving till the end of the linked list)


        """
        curr = head
        prev = None

        while curr:
            temp = curr.next  ## temp pointer 
            curr.next = prev  ## switches the nodes and keeps moving till the end
            prev = curr        ## switches the pointer
            curr = temp         ## switches the pointer

        return prev    
