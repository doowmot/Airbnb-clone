class Space:
    # We initialise with all of our attributes
    # Each column in the table should have an attribute here
    def __init__(self, id, listing_id, name, description, price):
        self.id = id
        self.listing_id = listing_id
        self.name = name
        self.description = description
        self.price = price


    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    
    def __repr__(self):
        return f"Space({self.id}, {self.listing_id}, '{self.name}', {self.description}, {self.price})"


