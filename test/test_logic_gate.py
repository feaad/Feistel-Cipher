import utils.logic_gate as logic
import pytest

def test_and_op():
    result = logic.and_op('0011', '1101')
    assert result == '0001'