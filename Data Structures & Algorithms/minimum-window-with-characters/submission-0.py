from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Return the shortest contiguous substring of ``s`` containing
        every character from ``t``, including duplicate occurrences.

        Character comparisons are case-sensitive. Characters not present
        in ``t`` may appear inside the returned substring.

        Args:
            s: The string in which to search.
            t: The characters and frequencies required in the window.

        Returns:
            The shortest valid substring of ``s``. Returns an empty string
            if no valid substring exists.

        Time Complexity:
            O(len(s) + len(t)).
            Each pointer moves across ``s`` at most once.

        Space Complexity:
            O(k), where k is the number of distinct characters tracked.
        """
        if not s or not t or len(t) > len(s):
            return ""

        required_counts = Counter(t)       # build frequencies automatically from t
        window_counts = defaultdict(int)   # frequencies change as window moves

        # Number of distinct character requirements currently satisfied.
        formed = 0

        # Total number of distinct character requirements to satisfy.
        required = len(required_counts)

        left = 0

        # Store the best window as: length, left index, right index.
        best_length = len(s)+1 # > len(s)
        best_left = 0
        best_right = 0

        for right, char in enumerate(s):
            window_counts[char] += 1

            # This requirement becomes satisfied exactly when its required
            # frequency is reached. Extra occurrences must not increment formed.
            if (
                char in required_counts
                and window_counts[char] == required_counts[char]
            ):
                formed += 1

            # Shrink the window while all distinct requirements are satisfied.
            while formed == required:
                current_length = right - left + 1

                if current_length < best_length:
                    best_length = current_length
                    best_left = left
                    best_right = right

                left_char = s[left]
                window_counts[left_char] -= 1
                left += 1

                # The removed character's requirement has become unsatisfied.
                if (
                    left_char in required_counts
                    and window_counts[left_char] < required_counts[left_char]
                ):
                    formed -= 1

        if best_length == len(s)+1:
            return ""

        return s[best_left : best_right + 1]