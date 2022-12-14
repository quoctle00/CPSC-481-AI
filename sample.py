import pomegranate

from collections import Counter

from model import model

def generate_sample():
    #dictionary of samples
    sample = {}
    #dictionary of parents
    parents = {}

    #loop over all the states in topological order
    for state in model.states:
        #check for states which are conditional
        if isinstance(state.distribution,pomegranate.ConditionalProbability):
            sample[state.name] = state.distribution.sample(parent_values = parents)
        else:
            sample[state.name] = state.distribution.sample()
        #keep track of the sampled value in the parents mapping
        parents[state.distribution] = sample[state.name]
    return sample

N = 10000
data = []
for i in range(N):
    sample = generate_sample()
    if sample["bus"] == "delayed":
        data.append(sample["miss"])

    print(Counter(data))