from discount_applier import DiscountApplier


class MockNotifier:


    def notify(self, user, message):
        print(f"The user : {user} received {message}")



def test_apply_v1(capfd):
    mockNotifier = MockNotifier()
    discount = 25
    discountApplier = DiscountApplier(mockNotifier)
    users = [1, 2, 3]
    discountApplier.apply_v1(discount, users)
    out, err = capfd.readouterr()
    splitingOut = out.split('\n')
    for i in range(len(users)):
        assert splitingOut[i] == (f"The user : {users[i]} received You've got a new discount of {discount}%")

def test_apply_v2(capfd):

    mockNotifier = MockNotifier()
    discount = 25
    discountApplier = DiscountApplier(mockNotifier)
    users = [1, 2, 3]
    discountApplier.apply_v2(discount, users)
    out, err = capfd.readouterr()
    splitingOut = out.split('\n')
    for i in range(len(users)):
        assert splitingOut[i] == (f"The user : {users[i]} received You've got a new discount of {discount}%")

    # TODO: write a test that fails due to the bug in
    # DiscountApplier.apply_v2
