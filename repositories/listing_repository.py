from models.listing import Listing

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
    
    def create(self, listing):
        self._connection.execute("INSERT INTO listings (user_id) VALUES (%s)", [listing.user_id])
        return None
    
    def delete(self, listing_id):
        self._connection.execute("DELETE FROM listings WHERE listing_id = %s", [listing_id])


    def update_listing(self, listing_id, column, new_value):
        match column:
            case "user_id":
                self._connection.execute(
                    "UPDATE listings SET user_id = %s WHERE listing_id = %s", 
                    (new_value, listing_id)
                )
            case _:
                raise ValueError(f"Unknown column: {column}")