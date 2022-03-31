import pytest

from sample_age import validate_age

def test_validate_age_valid_age():
    validate_age(-10)

def test_validate_age_invalid_age():
    with pytest.raises(ValueError, match="Age Cannot be less than 0"):
        validate_age(-1)