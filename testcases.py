import pytest
from unittest.mock import mock_open, patch
import string
from password_generator import generate_password, random_passphrase_generator

def test_generate_password_length():
    # Test the total length
    password = generate_password(3, 2, 1, 4, 10)
    assert len(password) == 10

def test_generate_password_composition():
    # Test the composition of the password
    l, u, p, d = 3, 2, 1, 4
    total = l + u + p + d
    password = generate_password(l, u, p, d, total)
    
    assert sum(c.islower() for c in password) == l
    assert sum(c.isupper() for c in password) == u
    assert sum(c.isdigit() for c in password) == d
    assert sum(c in string.punctuation for c in password) == p

def test_generate_password_edge_cases():
    # Test with some parameters as zero
    password = generate_password(5, 0, 0, 0, 5)
    assert len(password) == 5
    assert sum(c.islower() for c in password) == 5
    
    password = generate_password(0, 5, 0, 0, 5)
    assert len(password) == 5
    assert sum(c.isupper() for c in password) == 5

@patch('builtins.open', new_callable=mock_open, read_data="word1\nword2\nword3\nword4\nword5")
def test_random_passphrase_generator_word_count(mock_file):
    # Test that the passphrase has the correct number of words
    passphrase = random_passphrase_generator(3)
    assert len(passphrase.split()) == 3
    
    passphrase = random_passphrase_generator(1)
    assert len(passphrase.split()) == 1

@patch('builtins.open', new_callable=mock_open, read_data="word1\nword2\nword3\nword4\nword5")
def test_random_passphrase_generator_words_from_list(mock_file):
    # Test that the passphrase only contains words from our mocked list
    allowed_words = ["word1", "word2", "word3", "word4", "word5"]
    passphrase = random_passphrase_generator(4)
    
    for word in passphrase.split():
        assert word in allowed_words