from .dark_spellbook import dark_spellbook

def validate_ingredients(ingredients: str) -> str:
    allowed:list[str, str, str, str] = dark_spellbook.light_spell_allowed_ingredients()

    for allowed_ing in allowed:
        if allowed_ing in ingredients:
            return("Earth, wind and fire - VALID")