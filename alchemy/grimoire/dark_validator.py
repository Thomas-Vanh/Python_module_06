from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed_ingred: list[str] = dark_spell_allowed_ingredients()
    ingredient_lst: list[str] = ingredients.split()
    for ingredient in ingredient_lst:
        ingredient.lower()
        if ingredient in allowed_ingred:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
