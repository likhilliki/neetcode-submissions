class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.minFreq = 0
        self.keyToValFreq = {}
        self.freqToKeys = defaultdict(OrderedDict)

    def get(self, key: int) -> int:
        if key not in self.keyToValFreq:
            return -1
        value, freq = self.keyToValFreq[key]
        del self.freqToKeys[freq][key]
        if not self.freqToKeys[freq]:
            del self.freqToKeys[freq]
            if self.minFreq == freq:
                self.minFreq += 1
        self.keyToValFreq[key] = (value, freq + 1)
        self.freqToKeys[freq + 1][key] = None
        return value


    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.keyToValFreq:
            _, freq = self.keyToValFreq[key]
            self.keyToValFreq[key] = (value, freq)
            self.get(key)
            return
        if len(self.keyToValFreq) >= self.capacity:
            evict_key, _ = self.freqToKeys[self.minFreq].popitem(last=False)
            del self.keyToValFreq[evict_key]
        self.keyToValFreq[key] = (value, 1)
        self.freqToKeys[1][key] = None
        self.minFreq = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)