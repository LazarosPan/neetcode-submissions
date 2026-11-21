class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """Return the number of car fleets reaching the target."""

        # Pair each car's position with its corresponding speed and sort closest to target first
        cars = sorted(zip(position, speed), reverse=True)

        # Count how many independent fleets will reach the target
        fleets = 0

        # Store the arrival time of the fleet directly ahead
        slowest_time = 0

        # Process cars from closest to target to farthest from target
        for pos, spd in cars:

            # Calculate how many hours this car would need to reach the target alone
            time = (target - pos) / spd

            # A larger time means this car cannot catch the fleet ahead before the target
            if time > slowest_time:

                # Therefore, this car becomes the first car of a new fleet
                fleets += 1

                # Cars behind must now catch this fleet's arrival time to join it
                slowest_time = time

        # Return the total number of independent fleets
        return fleets