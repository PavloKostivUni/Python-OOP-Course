"""
Tests for CharField class
Command line: python -m pytest tests/unit/test_charfield.py
"""

import pytest
import project4


def make_test_class(_min_value, _max_value):
    obj = type('TestClass', (), {'name': project4.CharField(_min_value, _max_value)})
    return obj()


@pytest.fixture
def testClassValues():
    return {
        'name': "Pavlo"
    }


def test_get(testClassValues):
    obj = make_test_class(5, 100)
    obj.name = testClassValues['name']
    for attr_name in testClassValues:
        assert getattr(obj, attr_name) == testClassValues[attr_name]
    obj_class = type(obj)
    assert isinstance(obj_class.name, project4.CharField)

def test_set():
    min_value = 2
    max_value = 10
    obj = make_test_class(min_value, max_value)
    name_values = tuple('a' * i for i in range(min_value, max_value+1))
    for name in name_values:
        obj.name = name
        assert getattr(obj, 'name') == name

@pytest.mark.parametrize("name, exception", [("", ValueError), (7, TypeError), ("SuperLongName", ValueError)])
def test_set_invalid(name, exception):
    obj = make_test_class(1, 10)
    with pytest.raises(exception):
        obj.name = name

def test_set_name_min_length_only():
    min = 0
    max = None
    obj = make_test_class(min, max)
    name_values = tuple('a' * i for i in range(min, 100, 10))
    for name in name_values:
        obj.name = name
        assert getattr(obj, 'name') == name

def test_set_name_max_length_only():
    min = None
    max = 100
    obj = make_test_class(min, max)
    name_values = tuple('a' * i for i in range(0, max+1, 10))
    for name in name_values:
        obj.name = name
        assert getattr(obj, 'name') == name

def test_set_name_no_limits():
    min = None
    max = None
    obj = make_test_class(min, max)
    name_values = tuple('a' * i for i in range(0, 100, 10))
    for name in name_values:
        obj.name = name
        assert getattr(obj, 'name') == name