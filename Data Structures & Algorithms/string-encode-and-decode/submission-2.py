from typing import List


class Solution:

    def encode(self, strings: List[str]) -> str:
        # Store each string as: <length>#<string>
        return "".join(
            f"{len(string)}#{string}"
            for string in strings
        )

    def decode(self, encoded_string: str) -> List[str]:
        decoded_strings = []
        current_position = 0

        while current_position < len(encoded_string):
            # Find the separator after the length prefix.
            separator_position = encoded_string.find(
                "#",
                current_position
            )

            string_length = int(
                encoded_string[current_position:separator_position]
            )

            # Use the length to locate the string boundaries.
            string_start = separator_position + 1
            string_end = string_start + string_length

            decoded_strings.append(
                encoded_string[string_start:string_end]
            )

            # Move to the next encoded string.
            current_position = string_end

        return decoded_strings