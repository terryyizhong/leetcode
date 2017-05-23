'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
'''
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        currMin = self.getMin()
        if currMin is None or currMin > x:    # can not use not currMin becasue it could be 0
            currMin = x
        self.s.append((x, currMin))   # store currMin and curr element together


    def pop(self):
        """
        :rtype: void
        """
        self.s.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.s[-1][0] if self.s else None    # debug

    def getMin(self):
        """
        :rtype: int
        """
        if not self.s:    #debug
            return None
        return self.s[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
