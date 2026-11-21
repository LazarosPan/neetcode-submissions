class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """Return the number of car fleets reaching the target."""

        # Pair each position with its speed and sort cars from closest to farthest
        cars = sorted(zip(position, speed), reverse=True)

        # Store the arrival time of each independent fleet
        stack = []

        # Process cars from closest to target to farthest
        for pos, spd in cars:

            # Calculate when this car would reach the target by itself
            time = (target - pos) / spd

            # A slower arrival means this car cannot catch the fleet ahead
            if not stack or time > stack[-1]:

                # Add its arrival time because it creates a new fleet
                stack.append(time)

        # Each value in the stack represents one fleet
        return len(stack)