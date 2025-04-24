class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1 
        return temp

# Testing the Stack class and its methods
my_stack = Stack(1)

# Test 1: Push elements into the stack
print("Pushing values 2, 3, 4, 5, 6 into the stack...")
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.push(5)
my_stack.push(6)

# Test 2: Print the stack
print("Stack after pushing 5 values:")
my_stack.print_stack()

# Test 3: Pop an element from the stack
print("\nPopping one value from the stack...")
popped_node = my_stack.pop()
if popped_node:
    print(f"Popped value: {popped_node.value}")
else:
    print("Stack is empty, nothing to pop.")

# Test 4: Print the stack after popping an element
print("\nStack after popping one value:")
my_stack.print_stack()

# Test 5: Pop all elements and check behavior
print("\nPopping all elements from the stack...")
while my_stack.height > 0:
    popped_node = my_stack.pop()
    print(f"Popped value: {popped_node.value}")

# Test 6: Attempt to pop from an empty stack
print("\nAttempting to pop from an empty stack...")
popped_node = my_stack.pop()
if popped_node:
    print(f"Popped value: {popped_node.value}")
else:
    print("Stack is empty, nothing to pop.")

# Test 7: Print the stack when it's empty
print("\nStack after popping all values:")
my_stack.print_stack()
