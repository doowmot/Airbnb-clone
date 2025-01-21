from lib.booking import Booking

class BookingRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from bookings')
        bookings = []
        for row in rows:
            item = Booking(row["booking_id"], row["booking_status"], row["space_id"], row["date_id"], row["user_id"])
            bookings.append(item)
        return bookings
    
    def find(self, booking_id):
        rows = self._connection.execute(
            'SELECT * from bookings WHERE booking_id = %s', [booking_id])
        row = rows[0]
        return Booking(row["booking_id"], row["booking_status"], row["space_id"], row["date_id"], row["user_id"])