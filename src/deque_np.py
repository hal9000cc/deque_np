import numpy as np

class deque_np:

    def __init__(self, maxlen: int, shape: tuple, dtype: np.dtype):

        self.maxlen = maxlen
        self.array_size = maxlen + 1

        self.deque = np.array((self.array_size, *shape), dtype=dtype)
        self.start = 0
        self.position = 0

    def append(self, element):

        self.deque[self.position] = element
        self.position = (self.position + 1) % self.array_size

        if self.position == self.start:
            self.start = self.position + 1

    def __len__(self):
        return (self.position - self.start) % self.array_size
