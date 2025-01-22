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