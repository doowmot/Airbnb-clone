class Listing:
    def __init__(self, listing_id, user_id):
        self.listing_id = listing_id
        self.user_id = user_id

    def __repr__(self):
        return f"Listing({self.listing_id}, {self.user_id})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    
    