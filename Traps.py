# check if specified row and column are valid matrix index
from collections import deque


def isValid(i, j, N, M):
    return (0 <= i < M) and (0 <= j < N)

# Replace all O's in a matrix with their shortest distance
# from the nearest trap


def shortestDistanceToTraps(mat):
    # start writing from here

    # initializing queue as we are using BFS
    queue = deque()

    # initializing a result matrix which will store the final output
    # setting the value to 0
    result = [[0 for x in range(len(mat[0]))] for y in range(len(mat))]

    # setting the value T to 0 as distance is 0
    # if the value is not T set the value to -1
    for i in range(0, len(mat)):
        for j in range(0, len(mat[0])):
            if mat[i][j] == 'T':
                result[i][j] = 0
                queue.append((i, j, result[i][j]))
            else:
                result[i][j] = -1

    # to search the neighbours (left, down, right, up)
    row = [0, -1, 0, 1]
    col = [-1, 0, 1, 0]

    # while queue is not empty
    while queue:

        # implmenting queue First In First Out
        x, y, dist = queue.popleft()

        # checking if index exists and if the value is 'O' and is not visited
        # if yes then append to the queue and set the value in result matrix
        for i in range(len(row)):
            if isValid(row[i]+x, col[i]+y, len(mat[0]), len(mat)):
                if mat[row[i]+x][col[i]+y] == 'O' and result[row[i]+x][col[i]+y] == -1:
                    result[row[i]+x][col[i]+y] = dist + 1
                    queue.append((row[i]+x, col[i]+y, dist+1))

    return result


if __name__ == '__main__':

    mat = [
        ['O', 'O', 'T', 'O', 'O'],
        ['O', 'W', 'O', 'T', 'O'],
        ['W', 'T', 'O', 'O', 'W'],
        ['O', 'O', 'O', 'O', 'O']
    ]

    result = shortestDistanceToTraps(mat)

    # print results
    for r in result:
        print(r)
