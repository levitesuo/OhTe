from engine import game_engine
from services import gol_service

gol_service.create_board("200x200", "TESTER")
game_engine.start()
