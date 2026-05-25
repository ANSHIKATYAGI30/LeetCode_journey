from collections import deque

class MyStack(object):

    def __init__(self):

        self.q1 = deque()
        self.q2 = deque()


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """

        # Push into q2
        self.q2.append(x)

        # Move all elements from q1 to q2
        while self.q1:
            self.q2.append(self.q1.popleft())

        # Swap queues
        self.q1, self.q2 = self.q2, self.q1


    def pop(self):
        """
        :rtype: int
        """

        return self.q1.popleft()


    def top(self):
        """
        :rtype: int
        """

        return self.q1[0]


    def empty(self):
        """
        :rtype: bool
        """

        return len(self.q1) == 0
