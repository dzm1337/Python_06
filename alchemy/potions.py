import elements
from alchemy.elements import create_air, create_earth


def healing_potion() -> str:
    return (f"Healing potion brewed with "
            f"'{create_earth()}' and '{create_air()}'")


def strength_potion() -> str:
    return (f"Strenght potion brewed with '{elements.create_fire()}'"
            f"and '{elements.create_water()}'")
