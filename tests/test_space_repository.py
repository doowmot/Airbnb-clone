from lib.space_repository import SpaceRepository
from lib.space import Space
from lib.listing_repository import *

def test_get_all_spaces(db_connection):  
    db_connection.seed("seeds/makersbnb.sql")  
    repository = SpaceRepository(db_connection)  

    spaces = repository.all()

    assert spaces == [
        Space(1, "test_space_name", "test_space_description", 100, 1)
    ]

def test_create_space(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = SpaceRepository(db_connection)

    # Create a new space with a new name and description
    repository.create(Space(None, "Cozy Cabin", "A peaceful retreat in the woods", 200, 1))

    # Get all spaces and check that the new space is added
    result = repository.all()
    assert result == [
        Space(1, "test_space_name", "test_space_description", 100, 1),
        Space(2, "Cozy Cabin", "A peaceful retreat in the woods", 200, 1)
    ]


def test_delete_space(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = SpaceRepository(db_connection)

    # Delete the space with id=1
    repository.delete(1)

    # Get all spaces and check the space is removed
    result = repository.all()
    assert result == []


def test_update_space_name(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = SpaceRepository(db_connection)
    repository.update_space(1, "space_name", "test_name")
    result = repository.all()
    assert result == [
        Space(1, "test_name", "test_space_description", 100, 1)
    ]

def test_update_space_description(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = SpaceRepository(db_connection)
    repository.update_space(1, "space_description", "test_description")
    result = repository.all()
    assert result == [
        Space(1, "test_space_name", "test_description", 100, 1)
    ]

def test_update_space_price_per_night(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = SpaceRepository(db_connection)
    repository.update_space(1, "space_price_per_night", 1000)
    result = repository.all()
    assert result == [
        Space(1, "test_space_name", "test_space_description", 1000, 1)
    ]

def test_update_space_listing_id(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = SpaceRepository(db_connection)
    listing = ListingRepository(db_connection)
    listing.create(Listing(2, 1))
    repository.update_space(1, "listing_id", 2)
    result = repository.all()
    assert result == [
        Space(1, "test_space_name", "test_space_description", 100, 2)
    ]