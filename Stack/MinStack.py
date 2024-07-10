'''
We have to implement a stack and have an operation, getMin()
that gives us the minimum value in constant time
retriveing and adding values to a stack is alraedy constant time
to mkae get min constant, we can have 2 stacks
initilize the stack and minStack

when pushing to the stack, we have to push to min Stack too
we will push the current minimum value to the minStack

so, push(-2), 0, (-3)
Stack =             Min Stack = 
-3                  -3
0                   -2
-2                  -2
Min Stack will have the current min at each node
When we pop, we can just pop from both
and top just return stack[-1]
and getMin we can just return top of the minStack

'''


class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # append the minValue at each position to the minStack
        # see if top of minStack is the min or the new value
        minVal = min(val, self.minStack[-1] if self.minStack else val) 
        #if minStack is empty take value of val
        self.minStack.append(minVal)

    def pop(self) -> None:
        # pop from both stacks, minStack has a value at each position that holds the current min val
        self.stack.pop()
        self.minStack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        # minStack, the top of the stack holds its current min value
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
