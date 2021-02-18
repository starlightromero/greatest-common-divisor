"""Greatest Common Divisor Resursive Approach."""

def greatest_common_divisor(a, b):
    """Return the greatest common divisor of a and b."""
    if a == 0 or b == 0:
        return 0
    if a == b:
        return a
    if a > b:
        return greatest_common_divisor(a - b, b)
    return greatest_common_divisor(a, b - a)
