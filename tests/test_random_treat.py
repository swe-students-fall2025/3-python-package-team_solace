from snacktime import random_treat

def test_random_treat_deterministic():
    assert random_treat(seed=20) == random_treat(seed=20)

def test_random_treat_is_string():
    t = random_treat(seed=21)
    assert isinstance(t, str) and len(t) > 0

def test_random_treat_varies_with_seed():
    assert random_treat(seed=22) != random_treat(seed=23)

