import uuid


class Board:
    def __init__(self, size, name, grid_id=uuid.uuid4(), grid_data=None):
        self._id = str(grid_id)
        self._size = size
        if grid_data:
            self._grid = grid_data
        else:
            self._grid = [[0 for col in range(size)]
                          for row in range(size)]
        self._name = name

    def __str__(self):
        s = ""
        for y in range(self._size):
            for x in range(self._size):
                s += str(self._grid[y][x])
            s += "\n"
        return s

    def step(self):
        '''Applies game logic to the grid once.'''
        neigbour_grid = self._neighbour_grid()
        self._grid = self._new_grid_from_neighbours(neigbour_grid)
        return 1

    def manipulate(self, x: int, y: int):
        '''Turns cell (x, y) to 0 if it's 1 or to 1 if it's 0.'''
        if self._grid[y][x]:
            self._grid[y][x] = 0
        else:
            self._grid[y][x] = 1
        return 1

    def get_grid(self):
        '''Gets all the identifying info about the grid for it to be loaded again.'''
        return {"grid": self._grid, "name": self._name, "grid_id": self._id}

    # HOX maby redundant
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
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                      (0, 1), (1, -1), (1, 0), (1, 1)]

        for dx, dy in directions:
            new_x = x + dx
            new_y = y + dy

            # Check if neighbor is within grid bounds and not the cell itself
            if 0 <= new_x < self._size and 0 <= new_y < self._size:
                neighbours += self._grid[new_x][new_y]

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
