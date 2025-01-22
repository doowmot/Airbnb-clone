from models.date import *

class DateRepository:
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all dates
    def all(self):
        rows = self._connection.execute('SELECT * from dates')
        dates = []
        for row in rows:
            item = Date(row["date_id"], row["date"], row["available"], row["space_id"])
            dates.append(item)
        return dates

# Find a single user by their id
    def find(self, date_id):
        rows = self._connection.execute(
            'SELECT * from dates WHERE date_id = %s', [date_id])
        row = rows[0]
        return Date(row["date_id"], row["date"], row["available"], row["space_id"])


    def create(self, date):
        self._connection.execute('INSERT INTO dates (date, available, space_id) VALUES (%s,%s,%s)', [date.date, date.available, date.space_id])
        return None
    
    def delete(self, date_id):
        self._connection.execute("DELETE FROM dates WHERE date_id = %s", [date_id])
        return None
    
    def update_date(self, date_id, column, new_value):
        match column:
            case "date":
                self._connection.execute(
                    "UPDATE dates SET date = %s WHERE date_id = %s", 
                    (new_value, date_id)
                )
            case "available":
                self._connection.execute(
                    "UPDATE dates SET available = %s WHERE date_id = %s", 
                    (new_value, date_id)
                )
            case "space_id":
                self._connection.execute(
                    "UPDATE dates SET space_id = %s WHERE date_id = %s", 
                    (new_value, date_id)
                )
            case _:
                raise ValueError(f"Unknown column: {column}")