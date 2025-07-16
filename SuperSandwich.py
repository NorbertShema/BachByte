'''

Problem 4: Super Sandwich
A regular at the deli has requested a new order made by merging two different sandwiches on the menu together. 
Given the heads of two linked lists sandwich_a and sandwich_b where each node in the lists contains a spell segment, 
write a recursive function merge_orders() that merges the two sandwiches together in the pattern:

a1 -> b1 -> a2 -> b2 -> a3 -> b3 -> ...

Return the head of the merged sandwich.

Evaluate the time and space complexity of your solution. 
Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
'''

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def merge_orders(sandwich_a, sandwich_b):
    if not sandwich_a:
        return sandwich_b
    if not sandwich_b:
        return sandwich_a
    

    next_a = sandwich_a.next
    next_b = sandwich_b.next

    sandwich_a.next = sandwich_b
    sandwich_b.next = merge_orders(next_a,next_b)


    return sandwich_a

    

sandwich_a = Node('Bacon', Node('Lettuce', Node('Tomato')))
sandwich_b = Node('Turkey', Node('Cheese', Node('Mayo')))
sandwich_c = Node('Bread')

print_linked_list(merge_orders(sandwich_a, sandwich_b))
print_linked_list(merge_orders(sandwich_a, sandwich_c))

## Time complexity O(n)
##Space Complexity O(n)




##Iterative method
## Time complexity O(n)
##Space Complexity O(1)


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def merge_orders(sandwich_a, sandwich_b):
    # If either list is empty, return the other
    if not sandwich_a:
        return sandwich_b
    if not sandwich_b:
        return sandwich_a

    # Start with the first node of sandwich_a
    head = sandwich_a
    
    # Loop through both lists until one is exhausted
    while sandwich_a and sandwich_b:
        # Store the next pointers
        next_a = sandwich_a.next
        next_b = sandwich_b.next
        
        # Merge sandwich_b after sandwich_a
        sandwich_a.next = sandwich_b
        
        # If there's more in sandwich_a, add it after sandwich_b
        if sandwich_a:
            sandwich_b.next = next_a
        
        # Move to the next nodes
        sandwich_a = next_a
        sandwich_b = next_b

    # Return the head of the new merged list
    return head