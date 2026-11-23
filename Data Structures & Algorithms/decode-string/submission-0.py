class Solution:
    def decodeString(self, s: str) -> str:
        """
        Decode a string encoded using the pattern k[encoded_string].

        The encoded_string may itself contain nested encodings.

        Example:
            "2[a3[b]]c"
            -> "abbbabbbc"

        We use a stack to remember:
        1. The string built before entering '['.
        2. How many times the bracketed substring should be repeated.

        Time Complexity:
            O(n + m), where n is the encoded input length and
            m is the decoded output length.

        Space Complexity:
            O(m), primarily for constructing the decoded string.
        """
        stack = []
        current_string = ""
        current_number = 0

        for char in s:
            if char.isdigit():
                # Numbers can contain multiple digits, e.g. "12[a]".
                current_number = current_number * 10 + int(char)

            elif char == "[":
                # Save the state before entering this nested section.
                stack.append((current_string, current_number))

                # Start decoding the new bracketed substring.
                current_string = ""
                current_number = 0

            elif char == "]":
                # Restore the state corresponding to this '['.
                previous_string, repeat_count = stack.pop()

                # Decode the current bracketed section.
                current_string = (
                    previous_string + current_string * repeat_count
                )

            else:
                # Normal lowercase letter.
                current_string += char

        return current_string