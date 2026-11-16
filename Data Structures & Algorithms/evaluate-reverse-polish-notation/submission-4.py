class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                # First pop is the second operand in the expression.
                first_pop = stack.pop()
                second_pop = stack.pop()

                if token == "+":
                    result = second_pop + first_pop
                elif token == "-":
                    result = second_pop - first_pop
                elif token == "*":
                    result = second_pop * first_pop
                else:
                    # int() truncates the division result toward zero.
                    result = int(second_pop / first_pop)

                stack.append(result)

            else:
                # Keep only integers in the stack.
                stack.append(int(token))

        return stack.pop()