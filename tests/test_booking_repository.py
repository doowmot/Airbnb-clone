from models.booking import *
from repositories.booking_repository import *
from repositories.date_repository import *
from repositories.user_repository import *


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


def test_create_booking(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = BookingRepository(db_connection)
    # Create a new booking
    repository.create(Booking(2, False, 1, 1, 1))
    # Get all bookings and check that the new booking is added
    result = repository.all()
    assert result == [
        Booking(1, True, 1, 1, 1),
        Booking(2, False, 1, 1, 1)
    ]

def test_delete_booking(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = BookingRepository(db_connection)
    # Delete the booking with id=1
    repository.delete(1)
    # Get all bookings and check the booking is removed
    result = repository.all()
    assert result == []


def test_update_booking_status(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = BookingRepository(db_connection)
    repository.update_booking(1, "booking_status", False)
    result = repository.all()
    assert result == [
        Booking(1, False, 1, 1, 1)
    ]

def test_update_booking_space_id(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = BookingRepository(db_connection)
    repository.update_booking(1, "space_id", 1)
    result = repository.all()
    assert result == [
        Booking(1, True, 1, 1, 1)
    ]


def test_update_booking_date_id(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = BookingRepository(db_connection)
    date = DateRepository(db_connection)
    date.create(Date(2, '2025-02-01', False, 1))
    repository.update_booking(1, "date_id", 2)
    result = repository.all()
    assert result == [
        Booking(1, True, 1, 2, 1)
    ]


def test_update_booking_user_id(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = BookingRepository(db_connection)
    user = UserRepository(db_connection)
    user.create(User(2, 'email', "password"))
    repository.update_booking(1, "user_id", 2)
    result = repository.all()
    assert result == [
        Booking(1, True, 1, 1, 2)
    ]
