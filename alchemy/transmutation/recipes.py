from ..potions import strength_potion
from alchemy.elements import create_air, create_earth
import elements


def lead_to_gold():
    return f"Recipe transmuting Lead to Gold: brew '{create_air()}' and {strength_potion()} mixed with '{elements.create_fire()}'"