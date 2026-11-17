class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:

            # Collision only happens:  +  -
            while stack and stack[-1] > 0 and asteroid < 0:
                previous = stack[-1]

                if previous < abs(asteroid):
                    # Previous asteroid explodes.
                    # Current asteroid may collide again.
                    stack.pop()
                    continue

                elif previous == abs(asteroid):
                    # Both explode
                    stack.pop()

                # Current asteroid explodes (or both exploded)
                break

            else:
                # No collision, or current asteroid survived all collisions
                stack.append(asteroid)

        return stack