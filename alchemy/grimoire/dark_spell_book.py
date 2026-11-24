from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list:
    return ["bats", "arsenic", "frogs", "eye-ball"]


def dark_spell_record(spell: str, ingredients: str):
    validation = validate_ingredients(ingredients)
    return f"Testing record light spell: Spell recorded: {spell} \
({ingredients} {validation[1]})"
