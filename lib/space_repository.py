from lib.space import Space

class SpaceRepository:
    def __init__(self, connection, user):
        self._connection = connection
        self.user = user

    def all(self):
        if not self.user.is_authenticated:
            return "Access denied. You must be signed in to view listings."
        rows = self._connection.execute('SELECT * FROM spaces')
        spaces = []
        for row in rows:
            space = Space(row['space_id'], row['space_name'], row['space_description'], row['space_price_per_night'], row['listing_id'])
            spaces.append(space)
        return spaces

    def create(self, space):
        if not self.user.is_authenticated:
            return "Access denied. You must be signed in to view listings."
        self._connection.execute('INSERT INTO spaces (space_name, space_description, space_price_per_night, listing_id) VALUES (%s, %s, %s, %s)', [
            space.space_name, space.space_description, space.space_price_per_night, space.listing_id])
        return None

    def find(self, space_id):
        if not self.user.is_authenticated:
            return "Access denied. You must be signed in to view listings."
        rows = self._connection.execute('SELECT * FROM spaces WHERE space_id = %s', [space_id])
        row = rows[0]
        return Space(row["space_id"], row["space_name"], row["space_description"], row["space_price_per_night"], row["listing_id"])

    def delete(self, space_id):
        if not self.user.is_authenticated:
            return "Access denied. You must be signed in to view listings."
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
    
    def create_with_dates(self, space, available_from, available_to):
        """Create a space and its availability dates"""
        if not self.user.is_authenticated:
            return "Access denied. You must be signed in to create listings."
        
        self._connection.execute(
            'INSERT INTO spaces (space_name, space_description, space_price_per_night, listing_id) VALUES (%s, %s, %s, %s) RETURNING space_id', 
            [space.space_name, space.space_description, space.space_price_per_night, space.listing_id]
        )
        
        space_id = self._connection.execute('SELECT lastval()')[0]['lastval']
        
        self._date_repository.create_availability_range(available_from, available_to, space_id)
        
        return space_id