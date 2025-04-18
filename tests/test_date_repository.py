from lib.date import *
from lib.date_repository import *
"""
When we call dateRepository#all
We get a list of User objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/makersbnb.sql") # Seed our database with some test data
    repository = DateRepository(db_connection) # Create a new dateRepository
    # Insert a new record
    db_connection.execute("INSERT INTO dates (date, available, space_id) VALUES (%s,%s,%s)", ['2025-02-01', False, 1])
    dates = repository.all() # Get all user
    # Check types of objects in the lists
    print("Type of returned date:", type(dates[0]))
    print("Type of expected date:", type(Date(1, '2025-01-01', True, 1)))
    print(type(Date(1, '2025-01-01', True, 1)))
    # Print out the actual and expected data for debugging
    print("Returned dates:", dates)
    print("Expected dates:", [
        Date(1, '2025-01-01', True, 1),
        Date(2, '2025-02-01', False, 1)
    ])
    assert repr(dates) == repr([
    Date(1, '2025-01-01', True, 1),
    Date(2, '2025-02-01', False, 1)
])

"""
When we call UserRepository#find
We get a single user object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = DateRepository(db_connection)

    db_connection.execute("INSERT INTO dates (date, available, space_id) VALUES (%s,%s,%s)", ['2025-02-01', False, 1])

    date = repository.find(2)
    assert repr(date) == repr(Date(2,"2025-02-01",False, 1))


def test_create_date(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = DateRepository(db_connection)
    # Create a new date
    repository.create(Date(2, '2025-02-01', False, 1))
    # Get all dates and check that the new date is added
    result = repository.all()
    assert repr(result) == repr([
        Date(1, '2025-01-01', True, 1),
        Date(2, '2025-02-01', False, 1)
    ])

def test_delete_date(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = DateRepository(db_connection)
    # Delete the booking with id=1
    repository.delete(1)
    # Get all bookings and check the booking is removed
    result = repository.all()
    assert result == []

def test_update_date(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = DateRepository(db_connection)
    repository.update_date(1, "date", '2025-03-01')
    result = repository.all()
    assert repr(result) == repr([
        Date(1, '2025-03-01', True, 1)
    ])

def test_update_available(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = DateRepository(db_connection)
    repository.update_date(1, "available", False)
    result = repository.all()
    assert repr(result) == repr([
        Date(1, '2025-01-01', False, 1)
    ])

def test_update_space_id(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = DateRepository(db_connection)
    repository.update_date(1, "space_id", 1)
    result = repository.all()
    assert repr(result) == repr([
        Date(1, '2025-01-01', True, 1)
    ])

def test_create_available_and_unavailable_dates(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = DateRepository(db_connection)
    
    repository.create(Date(1, "2025-01-01", True, 1))   # Available
    repository.create(Date(1, "2025-01-02", False, 1))  # Unavailable
    
    dates = repository.all()

    assert len(dates) == 3  # One date in the seed file + two addeed here

    assert dates[1].available == True
    assert dates[2].available == False

def test_create_availability_range(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = DateRepository(db_connection)

    initial_dates = repository.all()
    initial_count = len(initial_dates)

    repository.create_availability_range(
        available_from="2025-01-01",
        available_to="2025-01-03",
        space_id=1
    )

    dates = repository.all()

    assert len(dates) == initial_count + 3
    assert str(dates[1].date) == "2025-01-01"