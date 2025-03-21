"""
Tests for storage class
Command line: python -m pytest tests/unit/test_storage.py
"""
import pytest

from app.models import inventory


@pytest.fixture
def storage_values():
    return {
        'name': 'Thumbdrive',
        'manufacturer': 'Sandisk',
        'total': 10,
        'allocated': 3,
        'capacity_gb': 512
    }

@pytest.fixture
def storage(storage_values):
    return inventory.Storage(**storage_values)


def test_create(storage_values, storage):
    for attr_name in storage_values:
        assert getattr(storage, attr_name) == storage_values[attr_name]


@pytest.mark.parametrize("capacity_gb, exception", [(-1, ValueError), (0.5, TypeError), (0,ValueError)])
def test_create_invalid_capacity(capacity_gb, exception, storage_values):
    storage_values['capacity_gb'] = capacity_gb
    with pytest.raises(exception):
        inventory.Storage(**storage_values)


def test_repr(storage):
    assert storage.name in repr(storage)
    assert str(storage.capacity_gb) in repr(storage)