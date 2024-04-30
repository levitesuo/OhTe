from services import gol_service
from engine import game_engine
from entities.board import Board
import os
dirname = os.path.dirname(__file__)


def start_eng_from_file(filename):
    bint = 39
    grid = [[0 for row in range(bint)]for column in range(bint)]
    datasize = 39
    offset = (bint - datasize) // 2
    filepath = os.path.join(dirname, "text_patterns", filename)
    with open(filepath, "r") as f:
        data = f.read()
        data = data.split("\n")
        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] == "O":
                    grid[j+offset][i+offset] = 1

    gol_service._board = Board(bint, "From grid", grid_data=grid)
    game_engine.start()


start_eng_from_file("Max.txt")
