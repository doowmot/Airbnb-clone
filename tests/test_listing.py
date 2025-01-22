from lib.listing import *

def test_listing_constructs():
    listing = Listing(1,1)
    assert listing.listing_id == 1
    assert listing.user_id == 1


def test_listing_format_nicely():
    listing = Listing(1,1)
    assert str(listing) == "Listing(1, 1)"


def test_listings_are_equal():
    listing1 = Listing(1, 1)
    listing2 = Listing(1, 1)
    assert listing1 == listing2
