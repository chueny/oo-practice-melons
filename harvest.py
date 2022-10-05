############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, name,  first_harvest, color, is_seedless, is_bestseller, 
    ):
        """Initialize a melon."""

        self.pairings = [] #WHERE IS THIS FROM?
        self.code = code
        self.name = name
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)
        print(self.pairings)
        
    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code
        print(f"{self.code}")


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType(
        "musk",
        "Muskmelon",
        1998,
        "green",
        True,
        True
    )
    musk.add_pairing("mint")
    all_melon_types.append(musk)

    cas = MelonType("cas", "Casaba", 2003, "orange", False, False)
    cas.add_pairing("proscuitto")
    cas.add_pairing("strawberry")
    all_melon_types.append(cas)

    cren = MelonType(
        "cren",
        "Crenshaw",
        1996,
        "green",
        False,
        False
    )
    cren.add_pairing("prosciutto")
    all_melon_types.append(cren)
    
    watermelon = MelonType(
        "yw",
        "Yellow Watermelon",
        2013,
        "yellow",
        False,
        True
    )
    watermelon.add_pairing("ice cream")
    all_melon_types.append(watermelon)

   #print(f"{all_melon_types}")
   #if you print an objects, it prints a location in memory
    
    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
   
    # Fill in the rest
    for melon in melon_types:
        print(f"{melon.name} pairs with")
        for pairing in melon.pairings:
            print(f'- {pairing}')
        print()

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
