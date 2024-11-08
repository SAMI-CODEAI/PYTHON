# CREATING A LINKED LIST
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def append(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             return
#         last = self.head
#         while last.next:
#             last = last.next
#         last.next = new_node
#
#     def print_list(self):
#         current = self.head
#         while current:
#             print(current.data, end=" -> ")
#             current = current.next
#         print("None")
#
# if __name__ == "__main__":
#     ll = LinkedList()
#     ll.append(1)
#     ll.append(2)
#     ll.append(3)
#     ll.append(4)
#
#     print("Linked List:")
#     ll.print_list()  # Output: 1 -> 2 -> 3 -> 4 -> None
# # -----------------------------------------------------------
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution class to delete duplicates in a sorted linked list
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head

# Function to convert a list into a linked list
def list_to_linked_list(elements):
    if not elements:
        return None
    head = ListNode(elements[0])
    current = head
    for value in elements[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Function to convert a linked list back to a Python list
def linked_list_to_list(node):
    elements = []
    while node:
        elements.append(node.val)
        node = node.next
    return elements

# Main code to demonstrate the functionality
if __name__ == "__main__":
    # Take user input for the list
    input_str = input("Enter the elements of the list separated by spaces: ")
    input_list = list(map(int, input_str.split()))

    # Convert the list to a linked list
    linked_list_input = list_to_linked_list(input_list)

    # Create a Solution object and delete duplicates
    solution = Solution()
    result = solution.deleteDuplicates(linked_list_input)

    # Convert the result linked list back to a Python list
    result_list = linked_list_to_list(result)

    # Print the results
    print("Original list:", input_list)
    print("List after removing duplicates:", result_list)
