global n


def printGrid(grid):
    for r in range(n):
        for c in range(n):
            print(grid[r][c], end=" ")
        print()


def isValid(grid, r, c):
    for i in range(c):
        if grid[r][i] == 1:
            return False

    for i, j in zip(range(r, -1, -1), range(c, -1, -1)):
        if grid[i][j] == 1:
            return False

    for i, j in zip(range(r, n, 1), range(c, -1, -1)):
        if grid[i][j] == 1:
            return False

    return True


def placeQueen(grid, c):
    if c >= n:
        return True

    for r in range(n):
        if isValid(grid, r, c):

            grid[r][c] = 1

            if placeQueen(grid, c+1) == True:
                return True

            grid[r][c] = 0

    return False


def main():
    global n
    var = 0
    while (var < 4 or var > 8):
        var = int(input("Enter Grid size (n value): "))

    n = var
    grid = [[0]*n for i in range(n)]

    if placeQueen(grid, 0) == False:
        print("No solution possible.")
        return

    printGrid(grid)


main()
