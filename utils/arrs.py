import unittest

def get(array, index, default=None):

    if 0 <= index < len(array):
        return array[index]
    return default


def my_slice(coll, start=None, end=None):

    length = len(coll)

    if length == 0:
        return []

    if start is None:
        normalized_start = 0
    else:
        normalized_start = start

    if end is None or end > length:
        normalized_end = length
    else:
        normalized_end = end

    return coll[normalized_start:normalized_end]

