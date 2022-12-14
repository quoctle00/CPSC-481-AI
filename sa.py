import random

def randomSolution(tsp):
    cities = list(range(len(tsp)))
    solution = []

    for i in range(len(tsp)):
        randomCity = cities[random.randint(0,len(cities)-1)]
        solution.append(randomCity)
        cities.remove(randomCity)

    return solution

def routeLength(tsp,solution):
    routeLength = 0
    for i in range(len(solution)):
        routeLength += tsp[solution[i-1]][solution[i]]
    return routeLength

def simulateAnnealing(tsp):
    #set the currentState
    #for loop:
        #T = temperature
        #get the neighbours
        #calculate delta
        #if bestNeighbor better than currentStates
            #update currentState
        #else:
            #update currentState with some risk
    #return currentState

def main():
    print("howdeee doody")
    tsp = [
        [0,400,500,300],
        [400,0,300,500],
        [500,300,0,400],
        [300,500,400,0]
    ]

if __name__ == "__main__":
    main()