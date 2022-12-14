import math
from statistics import mean
from collections import Counter

def eucledianDistance(point1, point2):
    distance = 0

    for i in range(len(point1)):
        distance += math.pow(point1[i]-point2[i],2)
    return math.sqrt(distance)

def knn(dataset, query,k):

    neighbourDistanceAndIndex = []
    # Get the distance of query from each datapoint
    for index, dataPoint in enumerate(dataset):
        distance = eucledianDistance(dataPoint[:-1],query)

        # store index and distance of all the neighbours
        neighbourDistanceAndIndex.append((distance,index))
    # sort the list wrt distance
    sorted_neighbourDistanceIndex = sorted(neighbourDistanceAndIndex)
    # pick the first "k" nearest neighbours
    kNearestNeighboursDistanceIndices = sorted_neighbourDistanceIndex[:k]
    # get the "k" labels
    kNearestNeighboursLabels = [dataset[i][-1] for distance,i in kNearestNeighboursDistanceIndices]
    # get the most common label
    return mean(kNearestNeighboursLabels)

def main():
    queries = [[60],[63],[72],[65]]
    dataset = [
        [65.75,112.99],
        [71.52,136.49],
        [69.40,153.03],
        [68.22,142.34],
        [67.79,144.30],
        [68.70,123.30],
        [69.80,141.49],
        [70.01,136.46],
        [67.90,112.37],
        [66.49,127.45]
    ]

    for query in queries:
        prediction = knn(dataset,query,3)
        #for this height, the predicted weight is:
        print(round(prediction,2))


    if prediction == 1:
        print("Its gonna Rain!!!")
    else:
        print("NO Rain!!")
if __name__ == "__main__":
    main()