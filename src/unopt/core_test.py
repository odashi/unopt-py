import pytest

import unopt


def test_unwrap():
    obj = object()
    assert unopt.unwrap(obj) is obj


def test_unwrap_error():
    with pytest.raises(unopt.UnwrapError):
        unopt.unwrap(None)


def test_unwrap_or():
    obj = object()
    default = object()
    assert obj is not default
    assert unopt.unwrap_or(obj, default) is obj
    assert unopt.unwrap_or(None, default) is default


def test_unwrap_or_else():
    obj = object()
    default = object()
    assert obj is not default
    assert unopt.unwrap_or_else(obj, lambda: default) is obj
    assert unopt.unwrap_or_else(None, lambda: default) is default


def test_unwrap_unchecked():
    obj = object()
    assert unopt.unwrap_unchecked(obj) is obj
