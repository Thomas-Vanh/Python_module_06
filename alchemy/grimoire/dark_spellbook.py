from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    validation_res: str = validate_ingredients(ingredients)
    if "VALID" in validation_res:
        return f"Spell recorded: {spell_name} ({validation_res})"
    return f"Spell Rejected: {spell_name} ({validation_res})"
