from lib.user import *

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from users')
        users = []
        for row in rows:
            item = User(row["user_id"], row["user_email"], row["user_password"])
            users.append(item)
        return users

# Find a single user by their id
    def find(self, user_id):
        rows = self._connection.execute(
            'SELECT * from users WHERE user_id = %s', [user_id])
        row = rows[0]
        return User(row["user_id"], row["user_email"], row["user_password"])
    
    
    def create(self, user):
        self._connection.execute("INSERT INTO users (user_email, user_password) VALUES (%s, %s)", [user.user_email, user.user_password])
        return None
    
    def delete(self, user_id):
        self._connection.execute("DELETE FROM users WHERE user_id = %s", [user_id])


    def update_user(self, user_id, column, new_value):
        match column:
            case "user_email":
                self._connection.execute(
                    "UPDATE users SET user_email = %s WHERE user_id = %s", 
                    (new_value, user_id)
                )
            case "user_password":
                self._connection.execute(
                    "UPDATE users SET user_password = %s WHERE user_id = %s", 
                    (new_value, user_id)
                )
            case _:
                raise ValueError(f"Unknown column: {column}")