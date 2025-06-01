"""
Tests for IntegerField class
Command line: python -m pytest tests/unit/test_integerfield.py
"""

import pytest
import project4


def make_test_class(_min_value, _max_value):
    obj = type('TestClass', (), {'num': project4.IntegerField(_min_value, _max_value)})
    return obj()


@pytest.fixture
def testClassValues():
    return {
        'num': 25,
    }


def test_get(testClassValues):
    obj = make_test_class(5, 100)
    obj.num = testClassValues['num']
    for attr_name in testClassValues:
        assert getattr(obj, attr_name) == testClassValues[attr_name]
    obj_class = type(obj)
    assert isinstance(obj_class.num, project4.IntegerField)

def test_set():
    min_value = -5
    max_value = 10
    obj = make_test_class(min_value, max_value)
    num_values = range(min_value, max_value+1)
    for num in num_values:
        obj.num = num
        assert getattr(obj, 'num') == num

@pytest.mark.parametrize("num, exception", [(-10, ValueError), (75.5, TypeError), (600, ValueError)])
def test_set_invalid(num, exception):
    obj = make_test_class(-5, 100)
    with pytest.raises(exception):
        obj.num = num

def test_set_min_num_only():
    min = 0
    max = None
    obj = make_test_class(min, max)
    num_values = range(min, min+100, 10)
    for num in num_values:
        obj.num = num
        assert getattr(obj, 'num') == num

def test_set_max_num_only():
    min = None
    max = 10
    obj = make_test_class(min, max)
    num_values = range(max - 100, max+1, 10)
    for num in num_values:
        obj.num = num
        assert getattr(obj, 'num') == num

def test_set_num_no_limits():
    min = None
    max = None
    obj = make_test_class(min, max)
    num_values = range(-100, 100, 10)
    for num in num_values:
        obj.num = num
        assert getattr(obj, 'num') == num