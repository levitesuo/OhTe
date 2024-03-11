import uuid


class Board:
    def __init__(self, size, name):
        self._id = uuid.uuid4
        self._size = size
        self._grid = [[0 for col in range(size)]
                      for row in range(size)]
        self._name = name

    def step(self):
        '''Applies game logic to the grid once.'''
        neigbour_grid = self._neighbour_grid()
        self._grid = self._new_grid_from_neighbours(neigbour_grid)
        return 1

    def manipulate(self, x: int, y: int):
        '''Turns cell (x, y) to 0 if it's 1 or to 1 if it's 0.'''
        if self._grid[x][y]:
            self._grid[x][y] = 0
        else:
            self._grid[x][y] = 1
        return 1

    def get_grid(self):
        '''Gets all the identifying info about the grid for it to be loaded again.'''
        return {"grid": self._grid, "name": self._name, "grid_id": self._id}

    def load_grid(self, new_grid, name, grid_id):
        '''Loads the grid from '''
        if len(new_grid) != len(new_grid[0]):
            return "ERROR: The grid must be a square."
        for col in new_grid:
            for cell in col:
                if cell not in (0, 1):
                    return "ERROR: The grid must contain only zeros and ones."
        self._size = len(new_grid)
        self._grid = new_grid
        self._name = name
        self._id = grid_id
        return 1

    def _count_neighbours(self, x: int, y: int):
        '''Counts the amount of neighbours cell (x, y) has.'''
        neighbours = 0
        for i in range(-1, 2):
            # Skips rows that are not on the grid
            if not (x + i < 0 or x + i >= self._size):
                for j in range(-1, 2):
                    # Skips columns that are not on the grid.
                    # Also skips the cell itself.
                    if not (y + j < 0 or y + j >= self._size or (x == 0 and y == 0)):
                        neighbours += self._grid[x + j][y + i]
        return neighbours

    def _neighbour_grid(self):
        '''Creates a grid where the value of aclass Board:
     cell is the amount of neighbours it has.'''
        neigbour_grid = [[0 for col in range(self._size)]
                         for row in range(self._size)]
        # Count the amount of neighbours
        for y in range(self._size):
            for x in range(self._size):
                neigbour_grid[x][y] = self._count_neighbours(x, y)
        return neigbour_grid

    def _new_grid_from_neighbours(self, neighbour_grid):
        '''Given a grid of neighbours generates a new state for the grid.'''
        new_grid = [[0 for col in range(self._size)]
                    for row in range(self._size)]
        for y in range(self._size):
            for x in range(self._size):
                cell = neighbour_grid[x][y]
                if cell == 2:
                    new_grid[x][y] = self._grid[x][y]
                elif cell == 3:
                    new_grid[x][y] = 1
                elif cell < 2:
                    new_grid[x][y] = 0
                else:
                    cell = 0
        return new_grid
