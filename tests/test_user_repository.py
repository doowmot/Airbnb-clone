from lib.user import *
from lib.user_repository import *
"""
When we call UserRepository#all
We get a list of User objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/makersbnb.sql") # Seed our database with some test data
    repository = UserRepository(db_connection) # Create a new userRepository

        # Insert a new record
    db_connection.execute("INSERT INTO users (user_email, user_password) VALUES (%s,%s)", ["test2@gmail.com", "test_password2"])

    users = repository.all() # Get all user

    assert users == [
        User(1, "test@gmail.com", "test_password"),
        User(2, "test2@gmail.com", "test_password2")
    ]

"""
When we call UserRepository#find
We get a single user object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = UserRepository(db_connection)

    user = repository.find(1)
    assert user == User(1, "test@gmail.com", "test_password")