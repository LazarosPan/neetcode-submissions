from collections import deque


class MyStack:

    def __init__(self):
        # We use deque strictly as a queue:
        # append()  = push to back
        # popleft() = pop from front
        # q[0]      = peek at front
        self.q = deque()


    def push(self, x: int) -> None:
        # Queue operation: push the new element to the back.
        self.q.append(x)

        # Move all older elements from the front to the back.
        # This puts the newly added element at the front.
        #
        # Example:
        # Before pushing 3: [2, 1]
        # After append(3):  [2, 1, 3]
        #
        # First rotation:   [1, 3, 2]
        # Second rotation:  [3, 2, 1]
        #
        # Now 3, the stack's top, is at the queue's front.
        for _ in range(len(self.q) - 1):
            front = self.q.popleft()  # Pop from front.
            self.q.append(front)      # Push to back.


    def pop(self) -> int:
        # push() ensures that the newest element is at the front.
        # Therefore, popping from the front removes the stack's top.
        return self.q.popleft()


    def top(self) -> int:
        # Peek at the FRONT of the queue without removing it.
        #
        # q[0] is used because Python deque does not have
        # a method literally named peek().
        return self.q[0]


    def empty(self) -> bool:
        # Check whether the queue contains no elements.
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()