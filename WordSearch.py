# Below lists detail all eight possible movements from a cell
row = [-1, -1, -1, 0, 0, 1, 1, 1]
col = [-1, 0, 1, -1, 1, -1, 0, 1]


# Function to check if it is possible to go to position next
# from the current position. The function returns false if next is
# not in a valid position, or it is already visited
def isValid(mat, x, y, path):
    return (0 <= x < len(mat)) and (0 <= y < len(mat[0])) and (x, y) not in path


def DFS(mat, word, i, j, path=[], index=0):
    # Start writing from here
    # To check if the characters match at index
    # If no then return
    if mat[i][j] != word[index]:
        return

    # Include the current row and column value into the path
    path.append((i, j))

    # if the complete word is found then print and return
    if index == len(word) - 1:
        for i in range(0, len(path)):
            print(word[i], path[i], end=' ')
        print()
        # else check all the valid possilbe movements from the current position
    else:
        for k in range(len(row)):
            # if yes then call the function again and loop by increasing the index value to check the next postion
            if isValid(mat, i + row[k], j + col[k], path):
                DFS(mat, word, i + row[k], j + col[k], path, index + 1)

    # remove the last element from the path to backrack
    path.pop()


def WordSearch(mat, word):
    # base case
    if not mat or not len(mat) or not len(word):
        return

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            DFS(mat, word, i, j)


if __name__ == '__main__':

    mat = [
        ['A', 'D', 'E', 'B', 'C'],
        ['O', 'O', 'C', 'A', 'X'],
        ['S', 'C', 'D', 'K', 'C'],
        ['O', 'D', 'E', 'H', 'L']
    ]
    word = 'CODE'

    WordSearch(mat, word)
