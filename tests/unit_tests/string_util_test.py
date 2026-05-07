from app.string_utils import my_capitalize

# AAA-metoden
# Arrange, Act, Assert
def test_capitalize():
    # Arrange
    my_input = "kimmo"

    # Act
    result = my_capitalize(my_input)

    # Assert
    assert result == "Kmo"

def test_capitalize_with_empty_string():
    assert "" == my_capitalize("")

def test_capitalize_with_None():
    assert "" == my_capitalize(None)

def test_capitalize_with_numbers():
    assert "1Abc" == my_capitalize("1ABC")

def test_capitalize_with_single_characters():
    assert "A" == my_capitalize("a")
    assert "B" == my_capitalize("B")
    assert "1Abc" == my_capitalize("1ABC")
    assert "" == my_capitalize(None)
    assert "" == my_capitalize("")

import pytest

@pytest.mark.parametrize(
    "input, expected",
    [
        ("kimmo", "Kimmo"),
        ("  kimmo  ", "Kimmo"), # detta borde också fungera
        ("kimmo AHOLA", "Kimmo ahola"),
        ("a", "A"),
        ("1ABC", "1Abc"), # hade vänt på input och expected
        (None, ""), # samma här
        ("ÅÄÖ", "Åäö")
    ]
)
def test_capitalization(input, expected):
    assert my_capitalize(input) == expected