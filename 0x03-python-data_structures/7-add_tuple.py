#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    la, lb = len(tuple_a), len(tuple_b)
    nt = ((tuple_a[0] if la >= 1 else 0) +
                 (tuple_b[0] if lb >= 1 else 0),
                 (tuple_a[1] if la >= 2 else 0) +
                 (tuple_b[1] if lb >= 2 else 0))
    return nt
