import pytest
from files import converter 

def test_convert():
    assert converter.num2word (13453) == 'thirteen thousand, four hundred fifty three '
