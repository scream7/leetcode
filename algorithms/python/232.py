class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack1.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if not len(self.stack2):
            while len(self.stack1):
                self.stack2.append(self.stack1.pop())
        self.stack2.pop()

    def peek(self):
        """
        :rtype: int
        """
        if not len(self.stack2):
            while len(self.stack1):
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]
        
    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack1) == 0 and len(self.stack2) ==0

if __name__ == '__main__':
    q = Queue()
    #  q.push(1)
    #  q.push(2)
    #  print q.peek()
    #  q.push(3)
    #  print q.peek()

    #  q.push(1)
    #  q.push(2)
    #  print q.peek()

    q.push(1)
    print q.peek()
