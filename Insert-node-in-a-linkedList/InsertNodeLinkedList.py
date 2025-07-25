"""

You are given a class ListNode representing a node in a singly linked list, and a function print_linked_list
to print the linked list.
Your task is to implement the function insert that inserts a new node with a given value at a specified
position in the linked list.


Example 1: Insert in the middle

Input:
Linked list: 1 -> 2 -> 4
Insert value: 3
Position: 2

Output:
1 -> 2 -> 3 -> 4 -> None

Example 2: Insert in the middle of a two-node list
Input:
Linked list: 10 -> 20
Insert value: 15
Position: 1

Output:
10 -> 15 -> 20 -> None

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

def insert(head, value, position):
    new_node = ListNode(value)
    
    # If inserting at the head (position 0)
    if position == 0:
        new_node.next = head
        return new_node
    
    current = head
    current_position = 0
    
    # Traverse until the node before the desired position
    while current and current_position < position - 1:
        current = current.next
        current_position += 1
    
    if not current:
        raise IndexError("Position out of bounds")
    
    # Insert new_node between current and current.next
    new_node.next = current.next
    current.next = new_node
    
    return head

# Example 1
head = ListNode(1, ListNode(2, ListNode(4)))
head = insert(head, 3, 2)
print_linked_list(head)  # Output: 1 -> 2 -> 3 -> 4 -> None

# Example 2
head2 = ListNode(10, ListNode(20))
head2 = insert(head2, 15, 1)
print_linked_list(head2)  # Output: 10 -> 15 -> 20 -> None
