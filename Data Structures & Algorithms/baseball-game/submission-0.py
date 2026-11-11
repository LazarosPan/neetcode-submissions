class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for c in range(len(operations)):
            if operations[c] == "+":
                stack.append(stack[-1] + stack[-2])
            elif operations[c] == "D":
                stack.append(stack[-1] * 2)
            elif operations[c] == "C":
                stack.pop()
            else:
                stack.append(int(operations[c]))

        return sum(stack)