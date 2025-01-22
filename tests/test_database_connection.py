"""
When I seed the database
I get some records back
"""
def test_database_connection_spaces(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    db_connection.execute(
        "INSERT INTO spaces (space_name, space_description, space_price_per_night, listing_id) " 
        "VALUES (%s, %s, %s, %s)", ["Test Space", "A space for testing", 150, 1]
    )
    result = db_connection.execute("SELECT * FROM spaces")
    assert result == [
        {"space_id": 1, "space_name": "test_space_name", "space_description": "test_space_description", "space_price_per_night": 100, "listing_id": 1},
        {"space_id": 2, "space_name": "Test Space", "space_description": "A space for testing", "space_price_per_night": 150, "listing_id": 1}
    ]

def test_database_connection_users(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    db_connection.execute(
        "INSERT INTO users (user_email, user_password) VALUES (%s,%s)", 
        ["test2@gmail.com", "test_password2"]
    )
    result = db_connection.execute("SELECT * FROM users")
    assert result == [
        {"user_id": 1, "user_email": "test@gmail.com", "user_password": "test_password"},
        {"user_id": 2, "user_email": "test2@gmail.com", "user_password": "test_password2"}
    ]