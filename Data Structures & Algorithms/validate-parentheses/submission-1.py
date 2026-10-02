class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '(': ')',
            '[': ']',
            '{': '}',
        }

        stack = []

        for char in s:
            if char in pairs:
                # Store the opening bracket
                stack.append(char)
            else:
                # No opening bracket available
                if not stack:
                    return False

                opening = stack.pop()

                # Check whether it matches the closing bracket
                if pairs[opening] != char:
                    return False

        # No opening brackets should remain
        return len(stack) == 0