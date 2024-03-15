from engine import game_engine
from services import gol_service

gol_service.create_board("50x50", "TESTER")
game_engine.start()
