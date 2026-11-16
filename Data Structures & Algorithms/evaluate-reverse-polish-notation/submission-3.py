class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            result = 0
            if t == "+":
                result = int(stack.pop()) + int(stack.pop())
                stack.append(result)
            elif t == "-":
                result = - int(stack.pop()) + int(stack.pop())
                stack.append(result)
            elif t == "*":
                result = int(stack.pop()) * int(stack.pop())
                stack.append(result)
            elif t == "/":
                first = int(stack.pop())
                second = int(stack.pop())
                result = second / first
                stack.append(result)
            else:
                stack.append(t)

        return int(stack.pop())