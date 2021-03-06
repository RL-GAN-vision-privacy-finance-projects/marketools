import pytest
from marketools.analysis.price import relative_price_change


def test_relative_price_change__increase():
    result = relative_price_change(1.2, 0.8)
    assert 0.5 == pytest.approx(result)


def test_relative_price_change__decrease():
    result = relative_price_change(0.9, 1.2)
    assert -0.25 == pytest.approx(result)


def test_relative_price_change__zero():
    result = relative_price_change(19, 19)
    assert 0 == pytest.approx(result)
