from models.booking import Booking

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
    
    def create(self, booking):
        self._connection.execute('INSERT INTO bookings (booking_status, space_id, date_id, user_id) VALUES (%s,%s,%s,%s)', [booking.booking_status, booking.space_id, booking.date_id, booking.user_id])
        return None

    def delete(self, booking_id):
        self._connection.execute('DELETE FROM bookings WHERE booking_id = %s', [booking_id])


    def update_booking(self, booking_id, column, new_value):
        match column:
            case "booking_status":
                self._connection.execute(
                    "UPDATE bookings SET booking_status = %s WHERE booking_id = %s", 
                    (new_value, booking_id)
                )
            case "space_id":
                self._connection.execute(
                    "UPDATE bookings SET space_id = %s WHERE booking_id = %s", 
                    (new_value, booking_id)
                )
            case "date_id":
                self._connection.execute(
                    "UPDATE bookings SET date_id = %s WHERE booking_id = %s", 
                    (new_value, booking_id)
                )
            case "user_id":
                self._connection.execute(
                    "UPDATE bookings SET user_id = %s WHERE booking_id = %s", 
                    (new_value, booking_id)
                )
            case _:
                raise ValueError(f"Unknown column: {column}")