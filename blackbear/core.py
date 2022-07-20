from functools import reduce
import operator


def add_scalar(d:dict, value) -> dict:
    return {x: v + value for x, v in d.items()}


def add(d1:dict, d2:dict, fill=0) -> dict:
    return {x: v + d2.get(x, fill) for x, v in d1.items()}


def subtract_scalar(d:dict, value) -> dict:
    return {x: v - value for x, v in d.items()}


def subtract(d1:dict, d2:dict, fill=0) -> dict:
    return {x: v - d2.get(x, fill) for x, v in d1.items()}


def multiply_scalar(d:dict, value) -> dict:
    return {x: v * value for x, v in d.items()}


def multiply(d1:dict, d2:dict, fill=0) -> dict:
    return {x: v * d2.get(x, fill) for x, v in d1.items()}


def divide_scalar(d:dict, value) -> dict:
    return {x: v / value for x, v in d.items()}


def divide(d1:dict, d2:dict, fill=1) -> dict:
    return {x: v / d2.get(x, fill) for x, v in d1.items()}


def filter(d:dict, by: set):
    return {x: v for x, v in d.items() if x in by}


def sumv(d:dict):
    return sum(d.values())


def sumk(d:dict):
    return sum(d.keys())


def __product(iterable):
    return reduce(operator.mul, iterable, 1)


def productv(d:dict):
    return __product(d.values())


def productk(d:dict):
    return __product(d.keys())
