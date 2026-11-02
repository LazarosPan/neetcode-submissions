class MyHashMap:
    """Hash map with separate chaining and dynamically growing buckets."""

    def __init__(self):
        """Initialize an empty map with one bucket."""
        self._buckets = [[]]
        self._size = 0

    def put(self, key: int, value: int) -> None:
        """Insert or update a pair, growing the map when necessary."""
        bucket = self._buckets[key % len(self._buckets)]

        for index, (stored_key, _) in enumerate(bucket):
            if stored_key == key:
                bucket[index] = (key, value)
                return

        bucket.append((key, value))
        self._size += 1

        # Grow when the average number of entries per bucket exceeds one.
        if self._size > len(self._buckets):
            self._grow()

    def get(self, key: int) -> int:
        """Return the stored value, or -1 if the key is absent."""
        bucket = self._buckets[key % len(self._buckets)]

        for stored_key, stored_value in bucket:
            if stored_key == key:
                return stored_value

        return -1

    def remove(self, key: int) -> None:
        """Remove the key-value pair if it exists."""
        bucket = self._buckets[key % len(self._buckets)]

        for index, (stored_key, _) in enumerate(bucket):
            if stored_key == key:
                del bucket[index]
                self._size -= 1
                return

    def _grow(self) -> None:
        """Double capacity and redistribute all existing entries."""
        old_buckets = self._buckets
        self._buckets = [[] for _ in range(2 * len(old_buckets))]

        # Changing capacity changes the bucket index for existing keys.
        for bucket in old_buckets:
            for key, value in bucket:
                index = key % len(self._buckets)
                self._buckets[index].append((key, value))
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)