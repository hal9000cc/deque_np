import pytest
import numpy as np

from src.deque_np import deque_np

def test_fixed_type_deque():

    deque = deque_np(10, 1, np.float32)

    assert deque.maxlen == 10
    assert len(deque) == 0

    for i in range(10):
        deque.append(i * 10)
        assert  len(deque) == i

    deque.append(110)
    assert len(deque) == 10
