from logic import*

tuesday = Symbol("tuesday")   #it is a tuesday        (P)
rain = Symbol("raining")   #it is raining          (Q)
run = Symbol("run")       #Tom will go for a run  (R)

kb = And(Implication(And(tuesday, Not(rain)),run),
    tuesday,
    Not(rain)
    )

print(model_check(kb,run))

"""
who is the murder?
- there will be a chicken in the middle room
- 4 of you are to enter your own separate room
- in each of your room there will be a knife, and a light
- when the light turns green, it is killing time
- one of you is to kill the chicken and return to their room
- if no one kills the chicken within the time limit
    - all of you is eliminated
- if during the killing time, and there is more than 1 person in the midde room
    - those people are immediately eliminated, the game eneds
- after the killer returned to their room, the light will turn blue and the investigation begins
    - the participants may then leave their room
- the killer's goal is to not be caught, if succesful, they win and the rest lose
- if the killer is caught, they lose and the rest win.
"""