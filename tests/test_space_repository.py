from lib.space_repository import SpaceRepository
from lib.space import Space

def test_get_all_spaces(db_connection):  
    db_connection.seed("seeds/makersbnb.sql")  
    repository = SpaceRepository(db_connection)  

    spaces = repository.all()

    assert spaces == [
        Space(1, "test_space_name", "test_space_description", 100, 1)
    ]