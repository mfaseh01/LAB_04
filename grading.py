def get_grade(score):
    """Return a letter grade for a score between 0 and 100."""
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"
def apply_discount(price, discount_percent):
    """Return the final price after applying a percentage discount."""
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount must be between 0 and 100")
    return price - price * discount_percent / 100
