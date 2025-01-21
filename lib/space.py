class Space:

    def __init__(self, space_id, space_name, space_description, space_price_per_night, listing_id):

        if space_name == "":
            raise ValueError("Name cannot be empty")
        if not isinstance(space_name, str):
            raise ValueError("Name must be text")
        if space_price_per_night <= 0:
            raise ValueError("Price must be above 0")
        
        self.space_id = space_id
        self.space_name = space_name
        self.space_description = space_description
        self.space_price_per_night = space_price_per_night
        self.listing_id = listing_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return (
            f"Space("
            f"{self.space_id}, "
            f"'{self.space_name}', "
            f"'{self.space_description}', "
            f"{self.space_price_per_night}, "
            f"{self.listing_id}"
            ")"
    )
