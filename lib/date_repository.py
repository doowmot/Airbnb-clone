from lib.date import *

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
