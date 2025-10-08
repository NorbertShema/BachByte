# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # Understand:
            # - We are given the head of a linked list.
            # - The list may contain a cycle (a node’s next points back to a previous node).
            # - We need to return the node where the cycle begins, or None if there is no cycle.
        # - Constraints:
        #     - The linked list nodes have unique memory addresses (so identity comparison works).
        #     - Must do this with O(1) extra space.

        # Plan:
            # 1. Use Floyd’s Tortoise and Hare algorithm.
            # 2. Use two pointers: slow and fast.
            # 3. Move slow by one step, fast by two steps.
            # 4. If they meet, there is a cycle.
            # 5. Once a meeting point is found:
            #       - Set one pointer to head.
            #       - Move both pointers one step at a time.
            #       - The point where they meet again is the start of the cycle.
            # 6. If fast or fast.next becomes None, return None (no cycle).

        # Implement:

        if not head and head.next:
            return None  # empty list, no cycle

        slow = head
        fast = head

        # Phase 1: Detect if a cycle exists
        while fast and fast.next:
            slow = slow.next          # move slow by 1
            fast = fast.next.next     # move fast by 2

            if slow == fast:
                # Cycle detected, break and find the start of the cycle
                break
        else:
            # If loop exits normally (no break), no cycle
            return None

        # Phase 2: Find the start of the cycle
        slow = head  # reset one pointer to the start
        while slow != fast:
            slow = slow.next
            fast = fast.next

        # The node where they meet is the start of the cycle
        return slow
