from unittest.mock import MagicMock, Mock
from discount_applier import DiscountApplier


def notify(user, message):
    print(f"The user : {user} received {message}")


def test_apply_v1(capfd):
    mockNotifier = Mock(**{'notify.return_value': None, 'notify.side_effect': notify})
    discount = 25
    discountApplier = DiscountApplier(mockNotifier)
    users = [1, 2, 3]
    discountApplier.apply_v1(discount, users)
    out, err = capfd.readouterr()
    splitingOut = out.split('\n')
    for i in range(len(users)):
        assert splitingOut[i] == (f"The user : {users[i]} received You've got a new discount of {discount}%")

def test_apply_v2(capfd):
    mockNotifier = Mock(**{'notify.return_value': None, 'notify.side_effect': notify})
    discount = 25
    discountApplier = DiscountApplier(mockNotifier)
    users = [1, 2, 3]
    discountApplier.apply_v2(discount, users)
    out, err = capfd.readouterr()
    splitingOut = out.split('\n')
    for i in range(len(users)):
        assert splitingOut[i] == (f"The user : {users[i]} received You've got a new discount of {discount}%")
