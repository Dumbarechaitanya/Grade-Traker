"""Simple grade tracker utilities."""


def average(grades):
    """Return the average of a list of numeric grades."""
        if not grades:
            return 0
        return sum(grades) / len(grades)


def letter_grade(score):
    """Convert a numeric score (0-100) to a letter grade."""
    if score > 90:
        return "A"
    elif score > 80:
        return "B"
    elif score > 70:
        return "C"
    elif score > 60:
        return "D"
    return "F"


def highest(grades):
    """Return the highest grade."""
    return max(grades)
