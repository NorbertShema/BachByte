# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]

        Understand
                Input: list
                Output: a merged list
                Constraints:The number of nodes in both lists has a range [0, 50].
                Edge cases: empty list

        plan:
            -Use a dummy node to move and merge the nodes 

        Implement:    
        """       

        dummy = ListNode()  # dummy node to simplify edge cases
        current = dummy

    # Loop while both lists have nodes
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

    # Attach the remaining part
        current.next = list1 if list1 else list2

        return dummy.next   ##this is the head of the merged list.
        
    ##Time O(n)    
    ##Space O(1)