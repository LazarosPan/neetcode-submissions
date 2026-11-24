from collections import defaultdict


class FreqStack:
    """
    Stack-like data structure that removes the most frequent element.

    If multiple elements have the same maximum frequency, pop() returns
    the one pushed most recently among them.

    Data structures:
        freq[val]:
            Current frequency of `val`.

        group[f]:
            Stack of values in the order they reached frequency `f`.
            Its top is therefore the most recent value having frequency `f`.

        max_freq:
            Highest frequency currently present.

    Complexity:
        push: O(1)
        pop:  O(1)
        Space: O(n), where n is the number of pushes.
    """

    def __init__(self):
        # Maps each value to its current frequency.
        self.freq = defaultdict(int)

        # Maps frequency -> stack of values that reached that frequency.
        self.group = defaultdict(list)

        # Maximum frequency among all values currently in the stack.
        self.max_freq = 0

    def push(self, val: int) -> None:
        # Increment val's frequency.
        self.freq[val] += 1
        f = self.freq[val]

        # val most recently reached frequency f, so append it to that
        # frequency's stack. This preserves the required tie-breaking order.
        self.group[f].append(val)

        # Update the maximum frequency if necessary.
        self.max_freq = max(self.max_freq, f)

    def pop(self) -> int:
        # The last value to reach max_freq is the correct value to remove:
        # it has maximum frequency and is closest to the stack's top.
        val = self.group[self.max_freq].pop()

        # Its frequency decreases because one occurrence is removed.
        self.freq[val] -= 1

        # If nobody remains at this frequency, the maximum drops by one.
        if not self.group[self.max_freq]:
            self.max_freq -= 1

        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()