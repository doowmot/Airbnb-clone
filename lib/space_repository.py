from lib.space import Space

class SpaceRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM spaces')
        spaces = []
        for row in rows:
            space = Space(row['id'], row['listing_id'], row['name'], row['description'], row['price'])
            spaces.append(space)
        return spaces
    
    #Create a new space
    def create(self, space):
        self._connection.execute('INSERT INTO spaces (name, listing_id, description, price) VALUES (%s, %s, %s)', [
            space.listing_id, space.name, space.description, space.price])
        return None
    
    #Find a space
    def find(self, space_id):
        rows = self._connection.execute('SELECT * FROM spaces WHERE id = %s', [space_id])
        row = rows[0]
        return Space(row["id"], row["listing_id"], row["name"], row["description"], row["price"])
    
    #Delete a space
    def delete(self, space_id):
        self._connection.execute('DELETE FROM spaces WHERE id = %s', [space_id])
        return None