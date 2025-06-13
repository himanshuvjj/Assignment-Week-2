class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None  

class LinkedList:
    def __init__(self):
        self.head = None  

    def add_node(self, data):
        new_node = Node(data)
        if not self.head: 
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:  
            last_node = last_node.next
        last_node.next = new_node  

    def print_list(self):
        if not self.head:
            print("The list is empty.")
            return
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")  # indicate end of list

    def delete_nth_node(self, n):
        "(1-based index)."
        if not self.head:
            raise Exception("Cannot delete from an empty list.")
        
        if n < 1:
            raise Exception("Index must be a positive integer.")

        if n == 1:  
            self.head = self.head.next
            return

        current_node = self.head
        for _ in range(n - 2):  
            if current_node is None or current_node.next is None:
                raise Exception("Index out of range.")
            current_node = current_node.next
        
        if current_node.next is None:
            raise Exception("Index out of range.")
        
        current_node.next = current_node.next.next


    # Testing the implementation
if __name__ == "__main__":
    linked_list = LinkedList()
    
    linked_list.add_node(10)
    linked_list.add_node(20)
    linked_list.add_node(30)
    linked_list.add_node(40)
    linked_list.add_node(50)
    linked_list.add_node(60)
    linked_list.add_node(70)
    linked_list.add_node(80)
    
    print("Initial linked list:")
    linked_list.print_list()  

    print("Deleting the 2nd node:")
    linked_list.delete_nth_node(2)
    linked_list.print_list()  

    print("Deleting the 1st node:")
    linked_list.delete_nth_node(1)
    linked_list.print_list()  

    print("Deleting the 2nd node from the empty list:")
    linked_list.delete_nth_node(2) 
