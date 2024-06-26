

class Board:
    '''
    A class for creating and manipulating a grid for the game of life.

    Attributes
    ----------
    _id : str
        the id of the grid

    _name : str
        the name of the grid

    _size : int
        the size of the grid

    _grid : list
        the grid itself

    Methods

    step()
        Applies game logic to the grid once.

    manipulate(cord_x: int, cord_y: int)
        Turns cell (cord_x, cord_y) to 0 if it's 1 or to 1 if it's 0.

    get_grid()
        Gets all the identifying info about the grid for it to be loaded again.

    _count_neighbours(x: int, y: int)
        Counts the amount of neighbours cell (x, y) has.

    _neighbour_grid() 
        Creates a grid where the value of a cell its the number of its neighbours.

    _new_grid_from_neighbours(neighbour_grid)
        Given a grid of neighbours generates a new state for the grid.
    '''

    def __init__(self, size, name, grid_id=None, grid_data=None):
        self._id = str(grid_id)
        self._name = name
        self._size = size
        if grid_data:
            self._grid = grid_data
        else:
            self._grid = [[0 for col in range(size)]
                          for row in range(size)]

    def __str__(self):
        output_string = ""
        for i in range(self._size):
            for j in range(self._size):
                output_string += str(self._grid[i][j])
            output_string += "\n"
        return output_string

    def step(self):
        '''
        Applies game logic to the grid once.
        '''
        neigbour_grid = self._neighbour_grid()
        self._grid = self._new_grid_from_neighbours(neigbour_grid)

    def manipulate(self, cord_x: int, cord_y: int):
        '''
        Turns cell (cord_x, cord_y) to 0 if it's 1 or to 1 if it's 0.

        Parameters
        ----------
        cord_x : int
            the x coordinate of the cell to be manipulated

        cord_y : int
            the y coordinate of the cell to be manipulated
        '''
        if self._grid[cord_y][cord_x]:
            self._grid[cord_y][cord_x] = 0
        else:
            self._grid[cord_y][cord_x] = 1

    def get_grid(self):
        '''
        Gets all the identifying info about the grid for it to be loaded again.

        Returns
        -------
        dict
            a dictionary containing the grid, name and id of the grid
        '''
        return {"grid": self._grid, "name": self._name, "grid_id": self._id}

    def _count_neighbours(self, x: int, y: int):
        '''
        Counts the amount of neighbours cell (x, y) has.

        Parameters
        ----------
        x : int
            the x coordinate of the cell to be checked

        y : int
            the y coordinate of the cell to be checked

        Returns
        -------
        int
            the amount of neighbours cell (x, y) has
        '''
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
        '''
        Creates a grid where the value of a cell its the number of its neighbours.

        Returns
        -------
        list
            a grid where the value of a cell is the amount of neighbours it has
        '''
        neigbour_grid = [[0 for col in range(self._size)]
                         for row in range(self._size)]
        # Count the amount of neighbours
        for cord_y in range(self._size):
            for cord_x in range(self._size):
                neigbour_grid[cord_x][cord_y] = self._count_neighbours(

                    cord_x, cord_y)
        return neigbour_grid

    def _new_grid_from_neighbours(self, neighbour_grid):
        '''
        Given a grid of neighbours generates a new state for the grid.

        Parameters
        ----------
        neighbour_grid : list
            a grid where the value of a cell is the amount of neighbours it has

        Returns
        -------
        list
            a new grid with the new state of the cells
        '''
        new_grid = [[0 for col in range(self._size)]
                    for row in range(self._size)]
        for cord_y in range(self._size):
            for cord_x in range(self._size):
                cell = neighbour_grid[cord_x][cord_y]
                if cell == 2:
                    new_grid[cord_x][cord_y] = self._grid[cord_x][cord_y]
                elif cell == 3:
                    new_grid[cord_x][cord_y] = 1
                elif cell < 2:
                    new_grid[cord_x][cord_y] = 0
                else:
                    cell = 0
        return new_grid
