from app import is_valid_item


def test_valid_item_returns_true():
    assert is_valid_item("milk") is True


def test_empty_string_returns_false():
    assert is_valid_item("") is False


def test_whitespace_only_returns_false():
    assert is_valid_item("   ") is False


def test_non_string_returns_false():
    assert is_valid_item(None) is False
    assert is_valid_item(123) is False