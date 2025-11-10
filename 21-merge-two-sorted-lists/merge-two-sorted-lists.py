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

        Understand:
            - Input: We are given Two sorted linked lists (list1, list2)
            - Output: One merged sorted linked list
            - Constraints: 
                - The number of nodes in both lists is in range [0, 50]
                - Lists are sorted in non-decreasing order
            - Edge cases:
                - Either list could be empty
                - If Both lists empty → just return None

        Plan:
            - Use a dummy node to simplify the merge process
            - Maintain a pointer (current) to build the merged list
            - Compare nodes from both lists:
                - Attach the smaller one to current
                - Move forward in that list
            - Attach any remaining nodes once one list is exhausted
            - Return dummy.next as the head of the merged list
        """

        dummy = ListNode()   # dummy node to simplify edge cases
        current = dummy      # pointer to build the new list

        # Loop while both lists have nodes
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Attach whichever list is not empty (remaining nodes)
        current.next = list1 if list1 else list2

        # The head of the merged list is the next node after dummy
        return dummy.next

    # Time Complexity: O(n + m) → we traverse both lists once
    # Space Complexity: O(1) → no extra data structures, just pointers
