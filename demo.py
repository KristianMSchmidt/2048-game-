"""
Command line demo of AI-player.
Plays an entire game of 2048. 
"""
from backend.Game import Game

if __name__ == "__main__":
    num_games_to_play = 5
    results = []
    for i in range(num_games_to_play):
        game = Game(time_limit = 0.6)
        max_tile, move_num = game.autoplay()
        results.append((max_tile, move_num))
    print("[max_tile, num_moves]=", results)
    


