import pytest
from docs import wordlist

def test_wordlist():
    
    assert wordlist.congugation("awesomeness") == "22: They are: ['a', 'awe', 'e', 'en', 'ene', 'es', 'm', 'me', 'men', 'mene', 'n', 'ne', 'ness', 'o', 'om', 'omen', 's', 'so', 'some', 'we', '', '']"
