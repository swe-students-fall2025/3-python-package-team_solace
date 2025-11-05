# examples/demo.py

from snacktime import random_snack, random_treat, random_vegetable, recipe_salad

def main():
    print("=== snacktime demo ===")
    print("snack:", random_snack(seed=1))
    print("treat:", random_treat(seed=2))
    print("vegetable:", random_vegetable(seed=3))

    print("\n--- salad recipe ---")
    print(recipe_salad(serves=3, dressing="lemon"))

if __name__ == "__main__":
    main()
