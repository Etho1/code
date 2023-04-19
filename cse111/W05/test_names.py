from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    result = make_full_name("John", "Doe")
    assert result == "John Doe", f"Expected 'John Doe', but got {result}"

def test_extract_family_name():
    full_name = "John Doe"
    result = extract_family_name(full_name)
    assert result == "Doe", f"Expected 'Doe', but got {result}"

def test_extract_given_name():
    full_name = "John Doe"
    result = extract_given_name(full_name)
    assert result == "John", f"Expected 'John', but got {result}"
# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])