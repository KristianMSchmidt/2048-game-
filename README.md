# 2048-game-

Web app with an AI-player for the 2048-game

The AI-player is using minimax-search with pruning. The search is guided by a heuristics function, that to each
board position assigns a score reflecting the quality of the position.

As the game is indeterministic by nature (90% of new tiles have value 2, 10% have value 4), I've made the AI make decisions on expected-value scores E(X).

http://kristianmschmidt.pythonanywhere.com/twentyfortyeight
