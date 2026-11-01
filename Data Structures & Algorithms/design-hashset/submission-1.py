class MyHashSet:
    def __init__(self):
        # Each byte stores membership for 8 keys.
        # Round up to allocate enough bytes for all possible keys.
        self.bits = bytearray((1_000_001 + 7) // 8)

    def add(self, key: int) -> None:
        # Find the byte containing this key's bit.
        byte_index = key // 8

        # Find the bit's position within that byte: 0 through 7.
        bit_index = key % 8

        # Set that bit to 1, leaving all other bits unchanged.
        # Setting an already-set bit does nothing: no duplicates.
        self.bits[byte_index] |= 1 << bit_index

    def remove(self, key: int) -> None:
        byte_index = key // 8
        bit_index = key % 8

        # Clear this bit to 0, leaving other bits unchanged.
        # Clearing an already-zero bit does nothing.
        self.bits[byte_index] &= ~(1 << bit_index)

    def contains(self, key: int) -> bool:
        byte_index = key // 8
        bit_index = key % 8

        # Isolate this key's bit and check whether it is set.
        return (self.bits[byte_index] & (1 << bit_index)) != 0
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)