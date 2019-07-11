"""Advanced functions for calculator."""

from arithmetic import add, cube, multiply


# NOTE: to actually have these work, you'll need to copy these functions
# into arithmetic.py --- that's where calculator.py will look for them!


def add_mult(num1, num2, num3):
    """Add num1 and num2 and multiply sum by num3."""

    return multiply(add(num1, num2), num3)


def add_cubes(num1, num2):
    """Cube num1 and num2 and return the sum of these cubes."""

    return add(cube(num1), cube(num2))
