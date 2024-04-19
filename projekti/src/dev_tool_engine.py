from engine import game_engine
from services import gol_service

gol_service.create_board("20x20", "TESTER")
game_engine.start()
