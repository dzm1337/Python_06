import elements
from alchemy.elements import create_air, create_earth


def healing_potion():
    return f"Healing potion brewed with '{create_earth()}' and '{create_air()}'"

def strength_potion():
    return f"Strenght potion brewed with '{elements.create_fire()}' and '{elements.create_water()}'"