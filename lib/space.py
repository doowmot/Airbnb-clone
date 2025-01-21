class Space:
    # We initialise with all of our attributes
    # Each column in the table should have an attribute here
    def __init__(self, id, listing_id, name, description, price_per_night):

        if name == "":
            raise ValueError("Name cannot be empty")
        if not isinstance(name, str):
            raise ValueError("Name must be text")
        if price_per_night <= 0:
            raise ValueError("Price must be above 0")

        self.id = id
        self.listing_id = listing_id
        self.name = name
        self.description = description
        self.price_per_night = price_per_night

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Space({self.id}, {self.listing_id}, '{self.name}', '{self.description}', {self.price_per_night})"


