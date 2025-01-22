class User:
    def __init__(self, user_id, user_email,user_password):
        self.user_id = user_id
        self.user_email = user_email
        self.user_password = user_password

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    # This method makes it look nicer when we print an user
    def __repr__(self):
        return f"User({self.user_id}, {self.user_email}, {self.user_password})"