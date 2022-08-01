"""
Stack()
@description: creates a new empty stack, it needs no parameters
@params: no parameters needed
@return: an empty stack

push(item)
@description: appends item to the top of the stack, the stack is modified
@params: the item
@return: nothing

pop()
@description: removes the top item from the stack, the stack is modified
@params: no parameters needed
@return: the item

peek() / top()
@description: gets the top item from the stack
@params: no parameters needed
@return: the top item from the stack

size()
@description: gets the number of items on the stack
@params: no parameters needed
@return: the size of the stack

isEmpty()
@description: tests to see whether the stack is empty
@params: no parameters needed
@return: boolean
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedStack:
    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        if self.head == None:
            return True
        return False

    def size(self):
        return self.size

    def push(self, data):
        if self.head == None:
            self.head = Node(data)

        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")

        popped_node = self.head
        self.head = self.head.next
        popped_node.next = None

        return popped_node.data

    def peek(self):
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")

        return self.head.data


def testLinkedStack():
    s = LinkedStack()
    assert s.isEmpty() == True
    s.push(4)
    s.push(5)
    assert s.isEmpty() == False
    assert s.peek() == 5
    s.pop()
    assert s.peek() == 4


if __name__ == "__main__":
    testLinkedStack()
    print('ALL TEST CASES PASSED')