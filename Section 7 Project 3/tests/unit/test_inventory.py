"""
Tests for Resource class
Command line: python -m pytest tests/unit/test_resource.py
"""

import pytest

from app.models import inventory


@pytest.fixture
def resource_values():
    return{
        'name': "Rtx 3060 Ti",
        'manufacturer': "Nvidia",
        'total': 25,
        'allocated': 15
    }

@pytest.fixture
def resource(resource_values):
    return inventory.Resource(**resource_values)


def test_create_resource(resource_values, resource):
    for attr_name in resource_values:
        assert getattr(resource, attr_name) == resource_values[attr_name]


def test_create_invalid_total_type():
    with pytest.raises(TypeError):
        inventory.Resource("Rtx 3060 Ti", "Nvidia", 25.5, 15)

def test_create_invalid_allocated_type():
    with pytest.raises(TypeError):
        inventory.Resource("Rtx 3060 Ti", "Nvidia", 25, 15.5)

@pytest.mark.parametrize('total, allocated', [(25, -15), (25, 35)])
def test_create_invalid_allocated_value(total, allocated):
    with pytest.raises(ValueError):
        inventory.Resource("Rtx 3060 Ti", "Nvidia", total, allocated)

def test_total(resource):
    assert resource.total == resource._total

def test_allocated(resource):
    assert resource.allocated == resource._allocated

def test_availability(resource, resource_values):
    assert resource.available == resource.total - resource.allocated

def test_category(resource):
    assert resource.category == "resource"

def test_str_repr(resource):
    assert resource.name in str(resource)

def test_repr_repr(resource):
    assert repr(resource) == ("Resource name: {}; manufacturer: {};"
        " total amount: {}; allocated: {}").format(resource.name,
        resource.manufacturer, resource.total, resource.allocated
    )


def test_claim(resource):
    n = 2
    original_total = resource.total
    original_allocated = resource.allocated
    resource.claim(n)
    assert resource.total == original_total
    assert resource.allocated == original_allocated + n


@pytest.mark.parametrize('value', [-1, 0, 1000])
def test_claim_invalid(resource, value):
    with pytest.raises(ValueError):
        resource.claim(value)


def test_freeup(resource):
    n = 2
    original_total = resource.total
    original_allocated = resource.allocated
    resource.freeup(2)
    assert resource.total == original_total
    assert resource.allocated == original_allocated - n

@pytest.mark.parametrize('value', [-5, 0, 100])
def test_freeup_invalid(resource, value):
    with pytest.raises(ValueError):
        resource.freeup(value)


def test_died(resource):
    n = 2
    original_total = resource.total
    original_allocated = resource.allocated
    resource.died(2)
    assert resource.total == original_total - n
    assert resource.allocated == original_allocated - n

@pytest.mark.parametrize('value', [-5, 0, 100])
def test_died_invalid(resource, value):
    with pytest.raises(ValueError):
        resource.died(value)


def test_purchased(resource):
    n = 2
    original_total = resource.total
    original_allocated = resource.allocated
    resource.purchased(n)
    assert resource.total == original_total + n
    assert resource.allocated == original_allocated

@pytest.mark.parametrize('value', [-1, 0])
def test_purchase_invalid(resource, value):
    with pytest.raises(ValueError):
        resource.purchased(value)