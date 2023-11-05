import pytest
import main


def test_encoder():
    result = main.encrypt('10010011', 'AND', '1101')
    assert result == '00111000'
