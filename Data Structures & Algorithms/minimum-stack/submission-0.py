class MinStack:

    def __init__(self):
        self.stack = []      # Stores all pushed values
        self.min_stack = []  # Stores the minimum at each stack position


    def push(self, val: int) -> None:
        self.stack.append(val)

        # If this is the first value, it is automatically the minimum.
        # Otherwise, store whichever is smaller:
        # the new value or the previous minimum.
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))


    def pop(self) -> None:
        # Both stacks represent the same number of elements,
        # so when removing one value, remove its minimum as well.
        self.stack.pop()
        self.min_stack.pop()


    def top(self) -> int:
        # [-1] accesses the last (top) element in O(1).
        return self.stack[-1]


    def getMin(self) -> int:
        # The top of min_stack always contains the
        # minimum value of the entire current stack.
        return self.min_stack[-1]