from unittest.mock import MagicMock, Mock
from safe_calculator import SafeCalculator


def test_divide_should_not_raise_any_error_when_authorized():
    mockAuthorizer = Mock(**{"authorize.return_value": True})
    calculator = SafeCalculator(mockAuthorizer)
    assert calculator.add(1, 2) == 3
