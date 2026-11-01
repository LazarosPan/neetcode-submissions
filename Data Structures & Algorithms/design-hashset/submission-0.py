class MyHashSet:
    def __init__(self):
        # Initial capacity, not a fixed limit.
        # Each bucket is a separate list of keys.
        self.buckets = [[] for _ in range(8)]
        self.size = 0

    def add(self, key: int) -> None:
        # A set cannot contain duplicates.
        if self.contains(key):
            return

        # Double capacity before the table becomes over 75% full.
        # Keeping buckets short makes searches faster.
        if (self.size + 1) * 4 > len(self.buckets) * 3:
            self._resize(len(self.buckets) * 2)

        # Modulo maps any integer to a valid bucket index.
        index = key % len(self.buckets)
        self.buckets[index].append(key)
        self.size += 1

    def remove(self, key: int) -> None:
        # The key can only be in this bucket.
        index = key % len(self.buckets)
        bucket = self.buckets[index]

        for i in range(len(bucket)):
            if bucket[i] == key:
                # Replace the key with the bucket's last element.
                # Then pop the last element to avoid shifting items.
                # This also works when the key is already last.
                bucket[i] = bucket[-1]
                bucket.pop()
                self.size -= 1

                # Reclaim memory when the table becomes sparse.
                # Separate grow/shrink thresholds avoid repeatedly
                # resizing when keys are added and removed.
                if len(self.buckets) > 8:
                    if self.size * 8 < len(self.buckets):
                        self._resize(len(self.buckets) // 2)

                return

        # Missing key: nothing to remove.

    def contains(self, key: int) -> bool:
        # Search one bucket instead of the entire set.
        index = key % len(self.buckets)
        return key in self.buckets[index]

    def _resize(self, capacity: int) -> None:
        old_buckets = self.buckets
        self.buckets = [[] for _ in range(capacity)]

        # A new capacity changes key % capacity.
        # Redistribute all keys into their new buckets.
        for bucket in old_buckets:
            for key in bucket:
                index = key % capacity
                self.buckets[index].append(key)

        # self.size stays unchanged: no keys were added or removed.
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)