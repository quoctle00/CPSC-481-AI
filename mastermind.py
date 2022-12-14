#Members:
#Andrew Jung
#Jinendra Gambhir
#Tejaas Mukunda Reddy
#Quoc Le

from logic import *

colors = ["red", "blue", "green", "purple"]
symbols = []
for i in range(4):
    for color in colors:
        symbols.append(Symbol(f"{color}{i}"))

knowledge = And()

# Each color has a position.
for color in colors:
    knowledge.add(Or(
        Symbol(f"{color}0"),
        Symbol(f"{color}1"),
        Symbol(f"{color}2"),
        Symbol(f"{color}3")
    ))

# Only one position per color.
# there is only 4 position, so a nested for loop is implemented
# If the current color is not in this position, then it must be next
# code is very similar to puzzle.py
for color in colors:
    for position in range(4):
        for pos in range(4):
            if position != pos:
                knowledge.add(
                    Implication(Symbol(f"{color}{position}"), Not(Symbol(f"{color}{pos}")))
                )


# Only one color per position.
# nested for loop implemented, range is the number of color
# if the current color is not the same as the other color, then its in the other position
# implementation is very similar to puzzel.py
for posi in range(4):
    for c1 in colors:
        for c2 in colors:
            if c1 != c2:
                knowledge.add(
                    Implication(Symbol(f"{c1}{posi}"), Not(Symbol(f"{c2}{posi}")))
                )

# First Guess
knowledge.add(symbols[0])
knowledge.add(symbols[5])

# Second Guess
knowledge.add(Not(symbols[1]))
knowledge.add(Not(symbols[4]))
knowledge.add(Not(symbols[10]))
knowledge.add(Not(symbols[15]))

#We considered this option, but too much hardcoding and writing.
#knowledge.add(And(
#    Or(And(symbols[0], Not(symbols[4]), Not(symbols[8]), Not(symbols[12])), And(symbols[4], Not(symbols[0]), Not(symbols[8]), Not(symbols[12])), And(
#        symbols[8], Not(symbols[0]), Not(symbols[4]), Not(symbols[12])), And(symbols[12], Not(symbols[0]), Not(symbols[4]), Not(symbols[8]))),
#    Or(And(symbols[1], Not(symbols[5]), Not(symbols[9]), Not(symbols[13])), And(symbols[5], Not(symbols[1]), Not(symbols[9]), Not(symbols[13])), And(
#        symbols[9], Not(symbols[1]), Not(symbols[5]), Not(symbols[13])), And(symbols[13], Not(symbols[1]), Not(symbols[5]), Not(symbols[9]))),
#    Or(And(symbols[2], Not(symbols[6]), Not(symbols[10]), Not(symbols[14])), And(symbols[6], Not(symbols[2]), Not(symbols[10]), Not(symbols[14])), And(
#        symbols[10], Not(symbols[2]), Not(symbols[6]), Not(symbols[14])), And(symbols[14], Not(symbols[2]), Not(symbols[6]), Not(symbols[10]))),
#    Or(And(symbols[3], Not(symbols[7]), Not(symbols[11]), Not(symbols[15])), And(symbols[7], Not(symbols[3]), Not(symbols[11]), Not(symbols[15])), And(
#        symbols[11], Not(symbols[3]), Not(symbols[7]), Not(symbols[15])), And(symbols[15], Not(symbols[3]), Not(symbols[7]), Not(symbols[11])))
#))

#knowledge.add(And(
#    Or(And(symbols[0], Not(symbols[1]), Not(symbols[2]), Not(symbols[3])), And((symbols[4]), Not(symbols[5]), Not(symbols[6]), Not(symbols[7])), And(
#        (symbols[8]), Not(symbols[9]), Not(symbols[10]), Not(symbols[11])), And((symbols[12]), Not(symbols[13]), Not(symbols[14]), Not(symbols[15]))),
#    Or(And(symbols[1], Not(symbols[0]), Not(symbols[2]), Not(symbols[3])), And((symbols[5]), Not(symbols[4]), Not(symbols[6]), Not(symbols[7])), And(
#        (symbols[9]), Not(symbols[8]), Not(symbols[10]), Not(symbols[11])), And((symbols[13]), Not(symbols[12]), Not(symbols[14]), Not(symbols[15]))),
#    Or(And(symbols[2], Not(symbols[0]), Not(symbols[1]), Not(symbols[3])), And((symbols[6]), Not(symbols[4]), Not(symbols[5]), Not(symbols[7])), And(
#        (symbols[10]), Not(symbols[8]), Not(symbols[9]), Not(symbols[11])), And((symbols[14]), Not(symbols[12]), Not(symbols[13]), Not(symbols[15]))),
#    Or(And(symbols[3], Not(symbols[0]), Not(symbols[1]), Not(symbols[2])), And((symbols[7]), Not(symbols[4]), Not(symbols[5]), Not(symbols[6])), And((symbols[11]), Not(symbols[8]), Not(symbols[9]), Not(symbols[10])), And((symbols[15]), Not(symbols[12]), Not(symbols[13]), Not(symbols[14])))))


for symbol in symbols:
    if model_check(knowledge, symbol):
        print(symbol)
