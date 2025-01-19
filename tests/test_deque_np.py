import pytest
import time
import numpy as np
from collections import deque

from numpy.ma.core import append

from src.deque_np import deque_np

def test_deque_test():
    d = deque(maxlen=10)
    deque_test(d, 10, True)
    deque_test(d, 10)

def test_deque_np():
    d = deque_np(10, (1,), np.float32)
    deque_test(d, 10, True)
    deque_test(d, 10)

def deque_test(deque, size, is_empty = False):

    assert deque.maxlen == size
    assert len(deque) == 0 if is_empty else size

    for i in range(size):
        deque.append(i * 10 + 1)
        assert  len(deque) == i + 1 if is_empty else size
        assert deque[-1] == i * 10 + 1

    deque.append(110)
    assert len(deque) == size
    assert deque[-1] == 110

    deque.appendleft(99)
    assert  deque[0] == 99

    for i in range(size - 1):
        assert deque[i + 1] == (i + 1) * 10 + 1


@pytest.mark.parametrize('size', [1000000])
def test_performance(size):

    print('')

    test_deque = deque(maxlen=size)
    test_deque_np = deque_np(size, (1,), np.float32)

    performance_append(test_deque)
    performance_append(test_deque_np)

    performance_get_item(test_deque)
    performance_get_item(test_deque_np)

def performance_append(deque):

    time_start = time.time()

    for i in range(deque.maxlen):
        deque.append(1)

    print_performance_time(time_start, deque, f'append {deque.maxlen} elements')

def performance_get_item(deque):

    time_start = time.time()

    for i in range(deque.maxlen):
        _ = deque[i]

    print_performance_time(time_start, deque, f'get {deque.maxlen} elements')

def print_performance_time(time_start, deque, test_name):
    duration = time.time() - time_start
    print(f'{type(deque).__name__} {test_name}: {duration:.2f}')
