from alchemy.potions import healing_potion, strength_potion


def distilation():
    print("=== Distilation 0 ===")
    print("Direct access to alchemy/potions.py")
    print(f"Testing healing potion: \'{healing_potion()}\'")
    print(f"Testing stregnth potion: \'{strength_potion()}\'")


if __name__ == "__main__":
    distilation()
