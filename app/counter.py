def increment(value: int) -> int:
    return value + 1


def decrement(value: int) -> int:
    # Clamp at zero so non-positive inputs never go negative
    return max(value - 1, 0)
