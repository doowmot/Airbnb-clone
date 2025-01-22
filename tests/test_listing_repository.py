from models.listing import *
from repositories.listing_repository import *
from repositories.user_repository import *


def test_listing_get_all_records(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = ListingRepository(db_connection)

    db_connection.execute("INSERT INTO listings (user_id) VALUES (%s)", [1])

    listings = repository.all()
    assert listings == [
        Listing(1, 1),
        Listing(2, 1)
            ]


def test_get_single_record(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = ListingRepository(db_connection)

    listing = repository.find(1)
    assert listing == Listing(1, 1)

def test_create_listing(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = ListingRepository(db_connection)
    # Create a new listing
    repository.create(Listing(2, 1))
    # Get all listingss and check that the new listing is added
    result = repository.all()
    assert result == [
        Listing(1,1),
        Listing(2,1)
    ]

def test_delete_listing(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = ListingRepository(db_connection)
    # Delete the listing with id=1
    repository.delete(1)
    # Get all listings and check the listing is removed
    result = repository.all()
    assert result == []

def test_update_listing(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = ListingRepository(db_connection)
    user = UserRepository(db_connection)
    user.create(User(2, 'email', "password"))
    repository.update_listing(1, "user_id", 2)
    result = repository.all()
    assert result == [
        Listing(1, 2)
    ]