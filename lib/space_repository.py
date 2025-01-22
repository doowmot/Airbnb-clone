from lib.space import Space

class SpaceRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM spaces')
        spaces = []
        for row in rows:
            space = Space(row['space_id'], row['space_name'], row['space_description'], row['space_price_per_night'], row['listing_id'])
            spaces.append(space)
        return spaces

    #Create a new space
    def create(self, space):
        self._connection.execute('INSERT INTO spaces (space_name, space_description, space_price_per_night, listing_id) VALUES (%s, %s, %s, %s)', [
            space.space_name, space.space_description, space.space_price_per_night, space.listing_id])
        return None

    #Find a space
    def find(self, space_id):
        rows = self._connection.execute('SELECT * FROM spaces WHERE space_id = %s', [space_id])
        row = rows[0]
        return Space(row["space_id"], row["space_name"], row["space_description"], row["space_price_per_night"], row["listing_id"])

    #Delete a space
    def delete(self, space_id):
        self._connection.execute('DELETE FROM spaces WHERE space_id = %s', [space_id])
        return None
    

    def update_space(self, space_id, column, new_value):
        match column:
            case "space_name":
                self._connection.execute(
                    "UPDATE spaces SET space_name = %s WHERE space_id = %s", 
                    (new_value, space_id)
                )
            case "space_description":
                self._connection.execute(
                    "UPDATE spaces SET space_description = %s WHERE space_id = %s", 
                    (new_value, space_id)
                )
            case "space_price_per_night":
                self._connection.execute(
                    "UPDATE spaces SET space_price_per_night = %s WHERE space_id = %s", 
                    (new_value, space_id)
                )
            case "listing_id":
                self._connection.execute(
                    "UPDATE spaces SET listing_id = %s WHERE space_id = %s", 
                    (new_value, space_id)
                )
            case _:
                raise ValueError(f"Unknown column: {column}")