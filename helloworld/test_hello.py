#test runner
import pytest
from hello import add
def test_add():
    assert add(10,15) == 25
