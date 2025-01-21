from lib.listing import Listing

class ListingRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from listings')
        listings = []
        for row in rows:
            item = Listing(row["listing_id"], row["user_id"])
            listings.append(item)
        return listings
    
    def find(self, listing_id):
        rows = self._connection.execute(
            'SELECT * from listings WHERE user_id = %s', [listing_id])
        row = rows[0]
        return Listing(row["listing_id"], row["user_id"])