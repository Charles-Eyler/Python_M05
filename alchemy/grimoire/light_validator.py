def validate_ingredients(ingredients: str) -> tuple[str, str]:
    from .light_spell_book import light_spell_allowed_ingredients
    allowed = light_spell_allowed_ingredients()
    for ing in allowed:
        if ing in ingredients:
            return ingredients, "- VALID"
    else:
        return ingredients, "- INVALID"

