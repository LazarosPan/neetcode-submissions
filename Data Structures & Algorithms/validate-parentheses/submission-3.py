class Solution:
    def isValid(self, s: str) -> bool:
        """
        Return True if s contains valid parentheses/brackets.
        """

        if not s:
            return False

        # Closing -> opening bracket mapping
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        openings = {'(', '{', '['}

        stack = []

        for c in s:

            # Opening bracket
            if c in openings:
                stack.append(c)

            # Closing bracket
            elif c in pairs:
                if stack and stack[-1] == pairs[c]:
                    stack.pop()
                else:
                    return False

            # Invalid character
            else:
                return False

        # Valid only if every opening bracket was closed
        return not stack