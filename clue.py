from logic import *

# Symbols for the characters
mustard = Symbol("ColMustard")
plum = Symbol("ProfPlum")
scarlet = Symbol("MsScarlet")
characters = [mustard, plum, scarlet]

# Symbols for the rooms
kitchen = Symbol("Kitchen")
ballroom = Symbol("Ballroom")
library = Symbol("Library")
rooms = [kitchen,ballroom,library]

# Symbols for the weapons
knife = Symbol("knife")
revolver = Symbol("revolver")
wrench = Symbol("wrench")
weapons = [knife,revolver,wrench]

symbols = characters + rooms + weapons


def check_knowledge(knowledge):
    for symbol in symbols:
        if model_check(knowledge, symbol):
            print(f"{symbol}: YES")
        elif not model_check(knowledge, Not(symbol)):
            print(f"{symbol}: MAYBE")


# There must be a person, room, and weapon i.e. Rules of the game.
knowledge = And(
    Or(mustard,plum,scarlet),
    Or(ballroom,kitchen,library),
    Or(knife,revolver,wrench)
)

# Initial cards
knowledge.add(And(
    Not(mustard), Not(kitchen), Not(revolver)
)

)

# Unknown card
knowledge.add(Or(
    Not(scarlet), Not(library), Not(wrench)
))

# Known cards
knowledge.add(Not(plum))
knowledge.add(Not(ballroom))

check_knowledge(knowledge)
