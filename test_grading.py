import pytest
from grading import get_grade, apply_discount
 
def test_grade_a():
    assert get_grade(95) == "A"
 
def test_grade_b():
    assert get_grade(85) == "B"
 
def test_grade_f():
    assert get_grade(30) == "F"
 
def test_invalid_score():
    with pytest.raises(ValueError):
        get_grade(150)
 
def test_discount_20_percent():
    assert apply_discount(100, 20) == 80
