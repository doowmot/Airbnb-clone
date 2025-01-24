from lib.date import *

"""
Constructs with an date_id, date, date available, space_id
"""
def test_date_constructs():
    date = Date(1,"2025-01-01",True, 1)
    assert date.date_id == 1
    assert date.date == "2025-01-01"
    assert date.available == True
    assert date.space_id == 1

"""
We can format users to strings nicely
"""
def test_user_format_nicely():
    date = Date(1,"2025-01-01",True, 1)
    assert str(date) == "Date(1, 2025-01-01, True, 1)"

"""
Test dates are equal
"""
def test_dates_are_equal():
    date1 = Date(1,"2025-01-01",True, 1)
    date2 = Date(1,"2025-01-01",True, 1)
    assert date1 == date2
