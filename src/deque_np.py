import numpy as np

class deque_np:

    def __init__(self, maxlen: int, dtype: np.dtype, shape: tuple=(1,)):

        self.maxlen = maxlen
        self.array_size = maxlen + 1

        self.deque = np.zeros((self.array_size, *shape), dtype=dtype)
        self.clear()

    def append(self, element):

        self.deque[self.position] = element
        self.position = (self.position + 1) % self.array_size

        if self.position == self.start:
            self.start = self.position + 1

    def __len__(self):
        return (self.position - self.start) % self.array_size

    def clear(self):
        self.start = 0
        self.position = 0

    def appendleft(self, element):
        self.deque[self.start - 1] = element
        self.start = (self.start - 1) % self.array_size

        if self.position == self.start:
            self.position = self.position - 1

    def __getitem__(self, item):
        return self.deque[(self.start + (item % ((self.position - self.start) % self.array_size))) % self.array_size]

