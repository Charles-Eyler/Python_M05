from .dark_spell_book import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> tuple[str, str]:
    allowed = dark_spell_allowed_ingredients()
    for ing in allowed:
        if ing in ingredients:
            return ingredients, "- VALID"
    else:
        return ingredients, "- INVALID"
