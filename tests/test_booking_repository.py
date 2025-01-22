from lib.booking import *
from lib.booking_repository import *


def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/makersbnb.sql") # Seed our database with some test data
    repository = BookingRepository(db_connection) # Create a new userRepository

        # Insert a new record
    db_connection.execute("INSERT INTO bookings (booking_status, space_id, date_id, user_id) VALUES (%s,%s,%s,%s)", ["False", "1", "1", "1"])

    booking = repository.all() 

    assert booking == [
        Booking(1, True, 1, 1, 1),
        Booking(2, False, 1, 1, 1)
        ]


def test_booking_get_single_record(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = BookingRepository(db_connection)
    booking = repository.find(1)
    assert booking == Booking(1, True, 1, 1, 1)
