import pytest
from safe_calculator import SafeCalculator

class MockAuthorizer:
    def __init__(self, isAuthorized):
        self.isAuthorized = isAuthorized

    def authorize(self):
        return self.isAuthorized


def test_divide_should_not_raise_any_error_when_authorized():
    mockAuthorizer = MockAuthorizer(True)
    calculator = SafeCalculator(mockAuthorizer)
    assert calculator.add(1, 2) == 3
