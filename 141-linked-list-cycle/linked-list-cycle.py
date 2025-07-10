# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool

        plan:
            -Here I will use fast and slow pointer to check for a cycle, if they point on the same node, which will happen eventually then we have a cycle.
            - Think of pointer because they have a more efficent O(1) than sets that use O(n) time complexity
        """
        dummy = ListNode() ## this creates a dummy node
        dummy.next = head      ## this connects the dummy node to the head of the list
        slow, fast = dummy,dummy ## this intializes the two pointers to equal the dummy node created

        while fast and fast.next:
            fast = fast.next.next ## moves twice
            slow = slow.next        ## moves just once

            if slow is fast:
                return True       ## we have a cycle because fast has catched up to slow so return true

        return False        
        ## otherwise return false, no cycle