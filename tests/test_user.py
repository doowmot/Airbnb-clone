from lib.user import *


def test_user_constructs():
    user = User(1,"Jess23@gmail.com", "jj820")
    assert user.user_id == 1
    assert user.user_email == "Jess23@gmail.com"
    assert user.user_password == "jj820"

def test_user_format_nicely():
    user = User(1,"Jess23@gmail.com", "jj820")
    assert str(user) == "User(1, Jess23@gmail.com, jj820)"

def test_artists_are_equal():
    user1 = User(1,"Jess23@gmail.com", "jj820")
    user2 = User(1,"Jess23@gmail.com", "jj820")
    assert user1 == user2