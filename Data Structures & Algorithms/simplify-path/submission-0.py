class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        Simplify an absolute Unix-style path into its canonical form.

        Rules:
        - Ignore empty components caused by repeated '/'.
        - Ignore '.' because it represents the current directory.
        - '..' removes the most recent directory, when possible.
        - Everything else, including '...' or '....', is a valid name.

        Time: O(n), where n is the length of path.
        Space: O(n) for the directory stack.
        """
        directory_stack = []

        for component in path.split("/"):
            # Repeated slashes produce empty components; '.' changes nothing.
            if component == "" or component == ".":
                continue

            if component == "..":
                # We cannot move above the root directory.
                if directory_stack:
                    directory_stack.pop()
            else:
                # Normal directory/file name, including '...' and '....'.
                directory_stack.append(component)

        # Joining with one slash automatically removes duplicate/trailing slashes.
        return "/" + "/".join(directory_stack)