'''
we are given a string of tokens 
that has ints or arithmetic operation
we can have a stack in this problem to keep track of the numbers 
everytime we come across an operation, we can pop twice from the stack
save those numbers 
and perform the operation on those numbers we popped
and then append back to the stack the solution of the operation

so [2, 1, + , 3, *]
we only append to the stack when we have a number, when i is an operation, perform it
stack: [2, 1]
we reach the + 
pop twice, save the values, and append back to the stack
stack: [3, 3, *]
we reached *, so we pop twice again and solve the operation
and append the solution to the stack
stack: [9]
we can just return the top of the stack
Time: O(n)
Space: O(n)

'''

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i == "+":
                x = stack.pop()
                y = stack.pop()
                sums = y + x
                stack.append(sums)
            elif i == "-":
                x = stack.pop()
                y = stack.pop()
                diff = y - x
                stack.append(diff)
            elif i == "*":
                x = stack.pop()
                y = stack.pop()
                mult = y * x
                stack.append(mult)
            elif i == "/":
                x = stack.pop()
                y = stack.pop()
#getting wrong answer for division, 
# cause our division is giving us a float, so just turn float to an int

                quotient = int(y / x)
                stack.append(quotient) 
                #getting wrong answer for division, cause our division is giving us a float, so just turn float to an int

            #if its not an operation, just append the number to the stack
            else:
                stack.append(int(i))
        return stack[-1]
                        
            
