from models.booking import *

def test_booking_constructs():
    booking = Booking(1,True, 1, 1, 1)
    assert booking.booking_id == 1
    assert booking.booking_status == True
    assert booking.space_id == 1
    assert booking.date_id == 1
    assert booking.user_id == 1


def test_booking_format_nicely():
    booking = Booking(1, True, 1, 1, 1)
    assert str(booking) == "Booking(1, True, 1, 1, 1)"

def test_bookings_are_equal():
    booking1 = Booking(1,True, 1, 1, 1)
    booking2 = Booking(1,True, 1, 1, 1)
    assert booking1 == booking2