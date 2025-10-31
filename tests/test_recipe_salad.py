import pytest
from snacktime import recipe_salad

def test_recipe_includes_serves_and_ingredients():
    r = recipe_salad(serves=2, dressing="lemon")
    assert "Serves: 2" in r
    assert "Ingredients" in r
    assert "Dressing" in r

def test_recipe_bad_serves_raises():
    with pytest.raises(ValueError):
        recipe_salad(serves=0)

def test_recipe_dressing_variants():
    for d in ("lemon", "balsamic", "olive"):
        out = recipe_salad(serves=1, dressing=d)
        assert d in out.lower()
