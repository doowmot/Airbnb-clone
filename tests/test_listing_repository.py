from lib.listing import *
from lib.listing_repository import *


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