# This is an example of how to use the DatabaseConnection class

"""
When I seed the database
I get some records back
"""
def test_database_connection(db_connection):
    # Seed the database with some test data
    db_connection.seed("seeds/makersbnb.sql")

    # Insert a new record
    db_connection.execute("INSERT INTO users (user_email, user_password) VALUES (%s,%s)", ["test2@gmail.com", "test_password2"])

    # Retrieve all records
    result = db_connection.execute("SELECT * FROM users")

    # Assert that the results are what we expect
    assert result == [
        {"user_id": 1, "user_email": "test@gmail.com", "user_password": "test_password"},
        {"user_id": 2, "user_email": "test2@gmail.com", "user_password": "test_password2"}
    ]
