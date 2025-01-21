# This is an example of how to use the DatabaseConnection class

"""
When I seed the database
I get some records back
"""
def test_database_connection(db_connection):
    # Seed the database with some test data
    db_connection.seed("seeds/makersbnb.sql")

    # Insert a new record
    db_connection.execute("INSERT INTO spaces (space_name, space_description, space_price_per_night, listing_id) " 
                        "VALUES (%s, %s, %s, %s)", ["Test Space", "A space for testing", 150, 1])

    # Retrieve all records
    result = db_connection.execute("SELECT * FROM spaces")

    # Assert that the results are what we expect
    assert result == [
        {"space_id": 1, "space_name": "test_space_name", "space_description": "test_space_description", "space_price_per_night": 100, "listing_id": 1},
        {"space_id": 2, "space_name": "Test Space", "space_description": "A space for testing", "space_price_per_night": 150, "listing_id": 1}
    ]
