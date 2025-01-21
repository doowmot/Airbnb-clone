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