#!/etc/bin/env python
#coding:utf-8

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

class MinStack_lower(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.lenstack = 0
        self.minflag = False
        self.minelement = None
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """ 
        self.stack.append(x)
        self.lenstack += 1
        if x < self.minelement:
            self.minflag = False
            self.minelement = x
        

    def pop(self):
        """
        :rtype: void
        """
        self.minflag = False
        if self.lenstack == 0:
            return None
        else:
            x = self.stack[self.lenstack - 1]
            del(self.stack[self.lenstack - 1])
            self.lenstack -= 1
            if x < self.minelement:
                self.minflag = False
            return x
        
        

    def top(self):
        """
        :rtype: int
        """
        if self.lenstack == 0:
            return None
        else:
            return self.stack[self.lenstack - 1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if self.minflag:
            return self.minelement
        elif self.lenstack == 0:
            return None
        tmp = self.stack[0]
        for x in self.stack:
            if x < tmp:
                tmp = x
        self.minflag = True
        self.minelement = tmp
        return self.minelement
        
        
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stacklist = []
        self.lenstack = 0
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        curmin = self.getMin()
        if (curmin == None) or (curmin > x):
            curmin = x
        self.stacklist.append((x, curmin))
        self.lenstack += 1
        

    def pop(self):
        """
        :rtype: void
        """
        if self.lenstack == 0:
            return None
        else:
            x = self.stacklist[self.lenstack - 1]
            del(self.stacklist[self.lenstack - 1])
            self.lenstack -= 1
            return x[0]
        

    def top(self):
        """
        :rtype: int
        """
        if self.lenstack == 0:
            return None
        else:
            return self.stacklist[self.lenstack - 1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        if self.lenstack == 0:
            return None
        else:
            return self.stacklist[self.lenstack - 1][1]
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-1)
obj.top()
print obj.getMin()
obj.push(1)
obj.top()
print obj.getMin()
obj.pop()
obj.pop()
obj.pop()
# obj.push(32)
# print str(obj.stack)
# obj.pop()
# print str(obj.stack)
# param_3 = obj.top()
# print param_3
# param_4 = obj.getMin()
# print param_4