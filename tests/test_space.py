from lib.space import Space

def test_space_constructs():
    space = Space(1, "The Oasis", "Enjoy views of the beach", 100, 1)
    assert space.space_id == 1 
    assert space.space_name == "The Oasis"
    assert space.space_description == "Enjoy views of the beach"
    assert space.space_price_per_night == 100
    assert space.listing_id == 1


def test_spaces_format_nicely():
    space = Space(1, "The Oasis", "Enjoy views of the beach", 100, 1)
    assert str(space) == "Space(1, 'The Oasis', 'Enjoy views of the beach', 100, 1)"


def test_spaces_are_equal():
    space1 = Space(1, "The Oasis", "Enjoy views of the beach", 100, 1)
    space2 = Space(1, "The Oasis", "Enjoy views of the beach", 100, 1)
    assert space1 == space2

