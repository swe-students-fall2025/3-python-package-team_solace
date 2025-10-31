from snacktime import random_snack

def test_random_snack_deterministic():
    assert random_snack(seed=1) == random_snack(seed=1)

def test_random_snack_membership():
    s = random_snack(seed=2)
    assert isinstance(s, str) and len(s) > 0

def test_random_snack_varies_with_seed():
    assert random_snack(seed=3) != random_snack(seed=4)
