class User():
    def __init__(self, db, password_validator):
        self.db = db
        self.password_validator = password_validator
        self.is_authenticated = False

    def register_new_account(self, username, password):
        if self.db.user_exists(username):
            return "Account already exists. Please log in."
        else:
            if not self.password_validator.is_valid(password):
                return "Password is invalid. It must be at least 8 characters long, contain a digit, an uppercase letter, and a special character."
            self.db.add_user(username, password)
            return "Account created successfully!"
        
    def sign_in(self, username, password):
        if not self.db.user_exists(username):
            return "Username does not exist. Please register."
        elif not self.db.validate_user(username, password):
            return "Password is incorrect. Access denied."
        self.is_authenticated = True
        return "Sign-in successful!"
    
    def list_space(self, name, description, price):
        if not self.is_authenticated:
            return "Access denied. You must be signed in to list a space."