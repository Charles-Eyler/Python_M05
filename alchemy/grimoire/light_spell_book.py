def light_spell_allowed_ingredients() -> list:
    return ["Earth", "Air", "Fire", "Water"]


def light_spell_record(spell: str, ingredients: str):
    from .light_validator import validate_ingredients
    validation = validate_ingredients(ingredients)
    return f"Testing record light spell: Spell recorded: {spell} \
({ingredients} {validation[1]})"
