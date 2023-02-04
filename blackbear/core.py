from typing import Dict, Set
from functools import reduce
import operator


def add_scalar(d: Dict, value) -> Dict:
    """
    Adds a scalar value (single value) to every value in the dictionary.

    Args:
        d: a dictionary with values that can be + by the value.
        value: a scalar value.

    Returns:
        A dictionary of the original keys, with value added to each value.

    Raises:
        TypeError or ValueError: depending bad passed values.
    """
    return {x: v + value for x, v in d.items()}


def add(d1: Dict, d2: Dict, fill=0) -> Dict:
    """
    Adds values (d1 + d2), aligned on d1s keys. Only keys from d1 are
    considered, if key from d1 is absent from d2, a fill value can optionally
    be used as the argument for +.

    Args:
        d1: a dictionary with values that are valid variables for +.
        d2: a dictionary with values that are valid variables for +.
        fill: a scalar value, used to fill-in for absent keys in d2.

    Returns:
        A dictionary of the original d1 keys, with each value + from d2.

    Raises:
        TypeError or ValueError: depending bad passed values.
    """
    return {x: v + d2.get(x, fill) for x, v in d1.items()}


def subtract_scalar(d: Dict, value) -> Dict:
    """
    Subtracts a scalar value (single value) from every value in the dictionary.

    Args:
        d: a dictionary with values that can be - by the value.
        value: a scalar value.

    Returns:
        A dictionary of the original keys, with value subtracted from each
        value.

    Raises:
        TypeError or ValueError: depending bad passed values.
    """
    return {x: v - value for x, v in d.items()}


def subtract(d1: Dict, d2: Dict, fill=0) -> Dict:
    """
    Subtracts values (d1 - d2), aligned on d1s keys. Only keys from d1 are
    considered, if key from d1 is absent from d2, a fill value can optionally
    be used as the argument for +.

    Args:
        d1: a dictionary with values that are valid variables for -.
        d2: a dictionary with values that are valid variables for -.
        fill: a scalar value, used to fill-in for absent keys in d2.

    Returns:
        A dictionary of the original d1 keys, with each value - d2.

    Raises:
        TypeError or ValueError: depending bad passed values.
    """
    return {x: v - d2.get(x, fill) for x, v in d1.items()}


def multiply_scalar(d: Dict, value) -> Dict:
    """
    Multiplies a scalar value (single value) by every value in the dictionary.

    Args:
        d: a dictionary with values that can be * by the value.
        value: a scalar value.

    Returns:
        A dictionary of the original keys, with each value multiplied by value.

    Raises:
        TypeError or ValueError: depending bad passed values.
    """
    return {x: v * value for x, v in d.items()}


def multiply(d1: Dict, d2: Dict, fill=0) -> Dict:
    """
    Multiplies values (d1 * d2), aligned on d1s keys. Only keys from d1 are
    considered, if key from d1 is absent from d2, a fill value can optionally
    be used as the argument for +.

    Args:
        d1: a dictionary with values that are valid variables for *.
        d2: a dictionary with values that are valid variables for *.
        fill: a scalar value, used to fill-in for absent keys in d2.

    Returns:
        A dictionary of the original d1 keys, with each value * d2.

    Raises:
        TypeError or ValueError: depending bad passed values.
    """
    return {x: v * d2.get(x, fill) for x, v in d1.items()}


def divide_scalar(d: Dict, value) -> Dict:
    """
    Divides every value in the dictionary by a scalar value (single value).

    Args:
        d: a dictionary with values that can be / by the value.
        value: a scalar value.

    Returns:
        A dictionary of the original keys, with each value divided by value.

    Raises:
        TypeError or ValueError: depending bad passed values.
    """
    return {x: v / value for x, v in d.items()}


def divide(d1: Dict, d2: Dict, fill=1) -> Dict:
    """
    Divides values (d1 / d2), aligned on d1s keys. Only keys from d1 are
    considered, if key from d1 is absent from d2, a fill value can optionally
    be used as the argument for +.

    Args:
        d1: a dictionary with values that are valid variables for /.
        d2: a dictionary with values that are valid variables for /.
        fill: a scalar value, used to fill-in for absent keys in d2.

    Returns:
        A dictionary of the original d1 keys, with each value / d2.

    Raises:
        TypeError or ValueError: depending bad passed values.
    """
    return {x: v / d2.get(x, fill) for x, v in d1.items()}


def filter(d: Dict, by: Set) -> Dict:
    """
    Filters a larger dict by the keys passed in.

    Args:
        d: a dictionary.
        by: a set, containing keys from the dictionary to be filtered by.

    Returns:
        A dictionary of with original values, filtered.

    Raises:
        TypeError or ValueError: depending bad passed values.
    """
    return {x: v for x, v in d.items() if x in by}


def sumv(d: Dict):
    """
    Sum dictionary on values.

    Args:
        d: a dictionary.

    Returns:
        Sum of dictionary values.
    """
    return sum(d.values())


def sumk(d: Dict):
    """
    Sum dictionary on keys.

    Args:
        d: a dictionary.

    Returns:
        Sum of dictionary keys.
    """
    return sum(d.keys())


def __product(iterable):
    return reduce(operator.mul, iterable, 1)


def productv(d: Dict):
    """
    Product of all dictionary values.

    Args:
        d: a dictionary.

    Returns:
        Product of all dictionary values.
    """
    return __product(d.values())


def productk(d: Dict):
    """
    Product of all dictionary keys.

    Args:
        d: a dictionary.

    Returns:
        Product of all dictionary keys.
    """
    return __product(d.keys())


def reset(d: Dict, value):
    """
    Sets all values in dictionary d to value.

    Args:
        d: a dictionary
        value: a value

    Returns:
        new dictionary with the keys of d, all set to values of value

    """
    return {x: value for x in d}
