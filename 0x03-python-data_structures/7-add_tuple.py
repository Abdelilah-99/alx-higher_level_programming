#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_sum = (tuple(sum(elements) for elements in zip(tuple_a, tuple_b)))
    return tuple_sum
