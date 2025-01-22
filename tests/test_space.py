from models.space import Space
import pytest

def test_space_constructs():
    """Space correctly constructs with an id, listing id, name, description and price per night"""
    space = Space(1, "The Oasis", "Enjoy views of the beach", 100, 1)
    assert space.space_id == 1 
    assert space.space_name == "The Oasis"
    assert space.space_description == "Enjoy views of the beach"
    assert space.space_price_per_night == 100
    assert space.listing_id == 1

def test_spaces_format_nicely():
    """Format spaces to strings for easier debugging"""
    space = Space(1, "The Oasis", "Enjoy views of the beach", 100, 1)
    assert str(space) == "Space(1, 'The Oasis', 'Enjoy views of the beach', 100, 1)"

def test_spaces_are_equal():
    """We can compare two identical spaces And have them be equal"""
    space1 = Space(1, "The Oasis", "Enjoy views of the beach", 100, 1)
    space2 = Space(1, "The Oasis", "Enjoy views of the beach", 100, 1)
    assert space1 == space2

def test_space_must_have_name():
    """Spaces cannot be created with empty name"""
    with pytest.raises(ValueError, match="Name cannot be empty"):
        Space(1, "", "Enjoy views of the beach", 100, 1)

def test_space_name_must_be_string():
    """Space name must be a string"""
    with pytest.raises(ValueError, match="Name must be text"):
        Space(1, 123, "Enjoy views of the beach", 100, 1)

def test_description_can_be_empty():
    """Test that description can be empty as this is acceptable"""
    space = Space(1, "The Oasis", "", 100, 1)
    assert space.space_description == ""

def test_space_must_have_positive_price():
    """Spaces must be created with a price greater than zero"""
    with pytest.raises(ValueError, match="Price must be above 0"):
        Space(1, "The Oasis", "Enjoy views of the beach", 0, 1)
from lib.space import Space
import pytest

def test_space_constructs():
    """Space correctly constructs with an id, listing id, name, description and price per night"""
    space = Space(1, "The Oasis", "Enjoy views of the beach", 100, 1)
    assert space.space_id == 1 
    assert space.space_name == "The Oasis"
    assert space.space_description == "Enjoy views of the beach"
    assert space.space_price_per_night == 100
    assert space.listing_id == 1

def test_spaces_format_nicely():
    """Format spaces to strings for easier debugging"""
    space = Space(1, "The Oasis", "Enjoy views of the beach", 100, 1)
    assert str(space) == "Space(1, 'The Oasis', 'Enjoy views of the beach', 100, 1)"

def test_spaces_are_equal():
    """We can compare two identical spaces And have them be equal"""
    space1 = Space(1, "The Oasis", "Enjoy views of the beach", 100, 1)
    space2 = Space(1, "The Oasis", "Enjoy views of the beach", 100, 1)
    assert space1 == space2

def test_space_must_have_name():
    """Spaces cannot be created with empty name"""
    with pytest.raises(ValueError, match="Name cannot be empty"):
        Space(1, "", "Enjoy views of the beach", 100, 1)

def test_space_name_must_be_string():
    """Space name must be a string"""
    with pytest.raises(ValueError, match="Name must be text"):
        Space(1, 123, "Enjoy views of the beach", 100, 1)

def test_description_can_be_empty():
    """Test that description can be empty as this is acceptable"""
    space = Space(1, "The Oasis", "", 100, 1)
    assert space.space_description == ""

def test_space_must_have_positive_price():
    """Spaces must be created with a price greater than zero"""
    with pytest.raises(ValueError, match="Price must be above 0"):
        Space(1, "The Oasis", "Enjoy views of the beach", 0, 1)