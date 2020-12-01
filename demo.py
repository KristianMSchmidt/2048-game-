"""
Command line demo of AI-player.
Plays an entire game of 2048. 
"""

if __name__ == "__main__":
    from backend.Game import Game
    game = Game(time_limit = 0.6)
    game.autoplay()


