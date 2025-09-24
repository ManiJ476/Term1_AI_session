import statistics

data = [1, 3, 3, 6, 7, 8, 9]


median_value = statistics.median(data)

print(f"The median is: {median_value}")

from contextlib import contextmanager
@contextmanager

def stat_med(data):
    for x in 