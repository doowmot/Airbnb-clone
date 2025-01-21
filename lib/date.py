from datetime import datetime

class Date:
    def __init__(self, date_id, date, available, space_id):
        self.date_id = date_id
        # If the date is a datetime object, format it as a string
        if isinstance(date, datetime):
            self.date = date.strftime('%Y-%m-%d')  # Convert to string
        else:
            self.date = date
        self.available = available
        self.space_id = space_id

    def __eq__(self, other):
        print(f"Comparing {self} with {other}")  # Log the comparison
        return (
        isinstance(other, Date)
        and self.date_id == other.date_id
        and self.date == other.date
        and self.available == other.available
        and self.space_id == other.space_id
    )

    # This method makes it look nicer when we print a date
    def __repr__(self):
        return f"Date({self.date_id}, {self.date}, {self.available}, {self.space_id})"
