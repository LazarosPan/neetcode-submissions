class Solution:

    def encode(self, strings: List[str]) -> str:
        encoded_string = ""

        for string in strings:
            encoded_string += f"{len(string)}#{string}"

        return encoded_string

    def decode(self, encoded_string: str) -> List[str]:
        decoded_strings = []
        current_position = 0

        while current_position < len(encoded_string):
            separator_position = current_position

            # Find the '#' separating the length from the string.
            while encoded_string[separator_position] != "#":
                separator_position += 1

            # The characters before '#' represent the string's length.
            length_text = encoded_string[
                current_position:separator_position
            ]
            string_length = int(length_text)

            # The actual string starts immediately after '#'.
            string_start = separator_position + 1
            string_end = string_start + string_length

            decoded_string = encoded_string[string_start:string_end]
            decoded_strings.append(decoded_string)

            # Continue decoding from the next length prefix.
            current_position = string_end

        return decoded_strings