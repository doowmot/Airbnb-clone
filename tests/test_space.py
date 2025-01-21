from lib.space import Space

def test_space_constructs():
    space = Space(1, 1, "The Oasis", "Enjoy views of the beach", 100)
    assert space.id == 1 
    assert space.listing_id == 1
    assert space.name == "The Oasis"
    assert space.description == "Enjoy views of the beach"
    assert space.price == 100


def test_spaces_format_nicely():
    space = Space(1, 1, "The Oasis", "Enjoy views of the beach", 100)
    assert str(space) == "Space(1, 1, 'The Oasis', 'Enjoy views of the beach', 100)"


def test_spaces_are_equal():
    space1 = Space(1, 1, "The Oasis", "Enjoy views of the beach", 100)
    space2 = Space(1, 1, "The Oasis", "Enjoy views of the beach", 100)
    assert space1 == space2

