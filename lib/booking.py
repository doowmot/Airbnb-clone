class Booking:
    def __init__(self, booking_id, booking_status, space_id, date_id, user_id):
        self.booking_id = booking_id
        self.booking_status = booking_status
        self.space_id = space_id
        self.date_id = date_id
        self.user_id = user_id

    def __repr__(self):
        return f"Booking({self.booking_id}, {self.booking_status}, {self.space_id}, {self.date_id}, {self.user_id})"
    
    def __eq__(self,other):
        return self.__dict__ == other.__dict__

