def average(numbers):
    """Return the average of a list of numbers."""

    if not numbers:
        return 0

    return sum(numbers) / len(numbers)