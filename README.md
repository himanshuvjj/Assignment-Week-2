Create a linked list using OOPs principles: 

Node Class: Represents a single node in the linked list, containing data and a pointer to the next node.

LinkedList Class: Manages the linked list with methods to add nodes, print the list, and delete nodes.
              ->add_node(data): Adds a new node with the specified data to the end of the list.
              ->print_list(): Prints the entire linked list.
              ->delete_nth_node(n): Deletes the nth node (1-based index) from the list, with exception handling for edge cases.
              
Testing: The main block tests the implementation by creating a linked list, adding nodes, and performing deletions while printing the list after each operation.

Exception Handling:
    The program raises exceptions for:
           ->Deleting from an empty list.
           ->Deleting a node with an index that is out of range.
           ->Attempting to delete a node with a non-positive index.
