import sys
from . import random_snack, random_vegetable, random_treat, recipe_salad, __version__

USAGE = """\
snacktime v{v}

Usage:
  snacktime snack            # random snack
  snacktime recipt           # simple salad recipe (accepts 'recipe' too)
  snacktime recipe           # same as 'recipt' (spelling friendly)
  snacktime vegitable        # random vegetable (accepts 'vegetable' too)
  snacktime vegetable        # same as 'vegitable'
  snacktime treat            # random sweet treat

Options:
  --seed N                   # deterministic output for snack/veg/treat
  --serves N                 # servings for the salad recipe (default 1)
  --dressing NAME            # lemon | balsamic | olive (default lemon)
"""

def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv:
        print(USAGE.format(v=__version__))
        return 0

    cmd = argv[0].lower().strip()
    args = argv[1:]

    # spelling-friendly aliases
    if cmd == "recipt":
        cmd = "recipe"
    if cmd == "vegitable":
        cmd = "vegetable"

    # parse simple flags
    def read_flag(name, cast=int, default=None):
        if name in args:
            i = args.index(name)
            try:
                return cast(args[i+1])
            except Exception:
                raise SystemExit(f"Invalid value for {name}")
        return default

    seed = read_flag("--seed", int, None)
    serves = read_flag("--serves", int, 2)          # default now 2
    dressing = read_flag("--dressing", str, "balsamic")

    if cmd == "snack":
        print(random_snack(seed=seed)); return 0
    if cmd == "vegetable":
        print(random_vegetable(seed=seed)); return 0
    if cmd == "treat":
        print(random_treat(seed=seed)); return 0
    if cmd == "recipe":
        print(recipe_salad(serves=serves, dressing=dressing)); return 0

    print(USAGE.format(v=__version__))
    return 1

if __name__ == "__main__":
    raise SystemExit(main())
