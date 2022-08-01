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


class DynamicArrayStack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        if self.isEmpty():
            return None
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def testDynamicArrayStack():
    s = DynamicArrayStack()
    assert s.isEmpty() == True
    s.push(4)
    s.push(5)
    assert s.isEmpty() == False
    assert s.top() == 5
    s.pop()
    assert s.top() == 4
    assert s.size() == 1


if __name__ == "__main__":
    testDynamicArrayStack()
    print('ALL TEST CASES PASSED')