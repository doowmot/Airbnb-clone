from lib.space_repository import SpaceRepository
from lib.space import Space

class MockAuthUser:
    def __init__(self, is_authenticated=True):
        self.is_authenticated = is_authenticated

def test_get_all_spaces(db_connection):  
    db_connection.seed("seeds/makersbnb.sql")  
    mock_user = MockAuthUser(is_authenticated=True)
    repository = SpaceRepository(db_connection, mock_user)
    result = repository.all()
    assert result == [
        Space(1, "test_space_name", "test_space_description", 100, 1)
    ]

def test_create_space(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    mock_user = MockAuthUser(is_authenticated=True)
    repository = SpaceRepository(db_connection, mock_user)
    repository.create(Space(None, "Cozy Cabin", "A peaceful retreat in the woods", 200, 1))
    result = repository.all()
    assert result == [
        Space(1, "test_space_name", "test_space_description", 100, 1),
        Space(2, "Cozy Cabin", "A peaceful retreat in the woods", 200, 1)
    ]

def test_delete_space(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    mock_user = MockAuthUser(is_authenticated=True)
    repository = SpaceRepository(db_connection, mock_user)
    repository.delete(1)
    result = repository.all()
    assert result == []