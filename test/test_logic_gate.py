import utils.logic_gate as logic
import pytest


def test_and_op():
    result = logic.and_op("0011", "1101")
    assert result == "0001"


def test_and_op_value_error():
    with pytest.raises(ValueError):
        logic.and_op("0011", "110")
