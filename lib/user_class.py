class User():
    def __init__(self, db, password_validator):
        self.db = db
        self.password_validator = password_validator

    def register_new_account(self, username, password):
        if self.db.user_exists(username):
            return "Account already exists. Please log in."
        else:
            if not self.password_validator.is_valid(password):
                return "Password is invalid. It must be at least 8 characters long, contain a digit, an uppercase letter, and a special character."
            self.db.add_user(username, password)
            return "Account created successfully!"
        
    def sign_in(self, username, password):
        return self.db.validate_user(username, password)