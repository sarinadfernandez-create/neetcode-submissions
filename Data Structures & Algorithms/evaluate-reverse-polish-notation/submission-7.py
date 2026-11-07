import operator #this is also useful
import math #using trunc operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # you add numbers to the stack (can there be more than two numbers between operands?) until you hit an operand
        # wait I think maybe we need to traverse the list backwards
        # no eliminated because that breaks pemdas, and i think we would need to go backwards and forwards, which would still be 
        #i put 1 and 2 in the stack, hit + and add them, so result is 3. then I append 3 to stack, append 3, hit *, multiply them and get nine, then append 9 to stack.
        #stack is going to hold the list of all elements that are going to be operated together
        #this means that the answer has to get appended to the stack after we complete the operation.
        #real question/action item here is how do I convert the strings into statements gonna make a helper function and if its really simple we will just put it in
        operations = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }
        stack = []
        if tokens: 
            result = tokens[0] 
        else:
            result = 0 # might need to do int
        
        for i,x in enumerate(tokens): #might not need this, this is each token
            if x =="+" or x =="-" or x=="/" or x=="*":
                result = (operations[x](stack[-2],stack[-1]))
                stack.pop()
                stack.pop()
                stack.append(math.trunc(result))
            else:
                stack.append(int(x))
        
        return int(result)

#reflection: learned about math.trunc and using operators to map string versions of operators to their actual action.