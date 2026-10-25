class Solution:
    def isValid(self, s: str) -> bool:
        """
        ) : (, } : {, ]:[

        Args:
            string of bracket characters

        Returns:
            true if s is a valid string, and false otherwise.

        The input string s is valid if and only if:
        Every open bracket is closed by the same type of close bracket.
        Open brackets are closed in the correct order.
        Every close bracket has a corresponding open bracket of the same type.
        """
        if not s:
            return False

        pairs = {')':'(', '}':'{', ']':'['}
        stack = []

        for c in s:
            if c in pairs:
                if stack and stack[-1] == pairs[c]:
                    stack.pop()
                else:
                    return False
            else:
                # Store the opening bracket
                stack.append(c)
            
        return True if not stack else False
            