import pytest
from hello import add
def test_add():
    res = add(10,15)
    assert  res == 25
