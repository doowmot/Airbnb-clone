from models.user import *
from repositories.user_repository import *
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


def test_create_user(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = UserRepository(db_connection)
    # Create a new listing
    repository.create(User(2, "test2@gmail.com", "test2_password"))  
    # Get all listingss and check that the new listing is added
    result = repository.all()
    assert result == [
        User(1, "test@gmail.com", "test_password"),
        User(2, "test2@gmail.com", "test2_password")
    ]

def test_delete_user(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = UserRepository(db_connection)
    # Delete the listing with id=1
    repository.delete(1)
    # Get all listings and check the listing is removed
    result = repository.all()
    assert result == []


def test_update_user(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = UserRepository(db_connection)
    repository.update_user(1, "user_email", "test3@gmail.com")
    result = repository.all()
    assert result == [
        User(1, "test3@gmail.com", "test_password")
    ]