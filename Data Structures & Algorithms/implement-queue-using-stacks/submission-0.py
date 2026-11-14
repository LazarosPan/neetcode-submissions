class MyQueue:

    def __init__(self):
        # New elements are always pushed here
        self.in_stack = []

        # Front of the queue is at the top of this stack
        self.out_stack = []

    def push(self, x: int) -> None:
        # O(1): push new element onto in_stack
        self.in_stack.append(x)

    def pop(self) -> int:
        # Prepare out_stack if necessary
        self._move()

        # Top of out_stack = front of queue
        return self.out_stack.pop()

    def peek(self) -> int:
        # Prepare out_stack if necessary
        self._move()

        # Look at the front without removing it
        return self.out_stack[-1]

    def empty(self) -> bool:
        # Queue is empty only if BOTH stacks are empty
        return not self.in_stack and not self.out_stack

    def _move(self) -> None:
        # Only transfer when out_stack is empty
        if not self.out_stack:
            # Reversing the order gives us FIFO:
            # in_stack  = [1, 2, 3]
            # out_stack = [3, 2, 1]
            #                       ^ front
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()