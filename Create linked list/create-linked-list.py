"""
Question:Create a linked list

Write a function create_linked_list(values) that creates a linked list from a list of
numbers, nums and returns the head of the linked list.

Example 1:
Input: nums = [1, 2, 3, 4, 5]
Output: 1 -> 2 -> 3 -> 4 -> 5 -> None

Example 2:
Input: nums = []
Output: None


"""

class Node:
 def __init__ (self, data=0 , next =None):
   self.data = data
   self.next = next

def create_linked_list(values):
    if not values:
       return None

    head = Node (values[0])
    current = head

    for val in values [1:]:
        current.next = Node(val)
        current= current.next
        
    return head

# Helper to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(f"{current.data} -> ", end="")
        current = current.next
    print("None")

# Example 1: pass in [1, 2, 3, 4, 5]
nums = [1, 2, 3, 4, 5]
head = create_linked_list(nums)
print_linked_list(head)