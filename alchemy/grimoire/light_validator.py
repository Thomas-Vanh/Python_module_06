def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    allowed_ingred: list[str] = light_spell_allowed_ingredients()
    ingredient_lst: list[str] = ingredients.split()
    for ingredient in ingredient_lst:
        ingredient.lower()
        if ingredient in allowed_ingred:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
