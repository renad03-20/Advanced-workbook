class Node:
    #this calss represents the node of the linked list 
    def __init__(self, price):
        self.price = price
        self.next = None

class Linked_list:
    #this calss represents the linked list 
    def __init__(self):
        self.head = None

    #adds a new price to the linked list 
    def add_price(self, price):
        new_node = Node(price)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    #prints the linked list
    def print_list(self):
        if self.head is None:
            print('The list is empty')
            return

        current = self.head
        while current is not None:
            print(current.price, end=' -> ')
            current = current.next
        print('None')

    #the iterative function: finds the max price in the linked list 
    def find_max_price_iteratively(self):
        if self.head is None:
            print('Empty list!')
            return None

        #itreating through the list to find the max price
        max_price = float('-inf')
        current = self.head
        while current is not None:
            if current.price > max_price:
                max_price = current.price
            current = current.next
        return max_price

    #the recursive function: finds the max price in the linked list
    def find_max_price_recursively(self, node=None, max_price=float('-inf')):
        if node is None:
            node = self.head

        if node is None:  # empty list for the base case 
            return max_price
        
        #recursively calling the function to find the max price
        max_price = max(max_price, node.price)  
        if node.next is None:  # Base case End of the list
            return max_price

        return self.find_max_price_recursively(node.next, max_price)

    # the Floyd's Tortoise and Hare algorithm to detect cycles in the linked list 
    def has_cycle(self):
        slow, fast = self.head, self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

# Testing
stock_prices = Linked_list()
stock_prices.add_price(1000)
stock_prices.add_price(1000000)
stock_prices.add_price(68690000)
stock_prices.add_price(36547600)
stock_prices.add_price(8756750)
stock_prices.add_price(68960)
stock_prices.print_list()

# Check for cycles before running recursive function
if stock_prices.has_cycle():
    print("The list has a cycle!")
else:
    max_iterative = stock_prices.find_max_price_iteratively()
    print(f"Max Price (Iterative): {max_iterative}")

    max_recursive = stock_prices.find_max_price_recursively()
    print(f"Max Price (Recursive): {max_recursive}")