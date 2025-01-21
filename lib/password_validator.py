import re

class PasswordValidator:
    def is_valid(self, password):
        if len(password) < 8:
            return False
        if not re.search(r'[A-Z]', password):
            return False
        if not re.search(r'[!@#$%?]', password):
            return False
        return True