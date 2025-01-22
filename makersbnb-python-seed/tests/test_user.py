from unittest.mock import MagicMock
import pytest
from lib.user_class import User

@pytest.fixture
def mock_db():
    db = MagicMock() # Mock object for db connection
    return db

@pytest.fixture
def mock_password_validator():
    password_validator = MagicMock()  # Mock object for password validator
    return password_validator

@pytest.fixture
def user(mock_db, mock_password_validator):
    return User(mock_db, mock_password_validator) # Inject both mock db and password_validator into the User class

def test_register_new_account_with_valid_password(user, mock_db):
    mock_db.user_exists.return_value = False
    response = user.register_new_account("testuser", "Valid123!")
    assert response == "Account created successfully!"
    mock_db.add_user.assert_called_once_with("testuser", "Valid123!")

def test_register_account_with_invalid_password(user, mock_db, mock_password_validator):
    mock_db.user_exists.return_value = False
    mock_password_validator.is_valid.return_value = False
    response = user.register_new_account("testuser", "invalid")
    assert response == "Password is invalid. It must be at least 8 characters long, contain a digit, an uppercase letter, and a special character."
    mock_db.add_user.assert_not_called()

def test_sign_in_success(user, mock_db):
    mock_db.validate_user.return_value = True
    assert user.sign_in("testuser", "password123") is True

def test_sign_in_failure(user, mock_db):
    mock_db.validate_user.return_value = False
    assert user.sign_in("testuser", "wrongpassword") is False