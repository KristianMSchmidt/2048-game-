# 2048-game-

Web app with an AI-player for the 2048-game

The AI-player is using minimax-search with pruning.  
The search is guided by a heuristics function, that to each
board position assigns a score reflecting the quality of the position.

The game is indeterministic by nature - after each move by the player, the computer randomly selects a free position to place a new tile - 90% of these new tiles will have value 2, while 10% will have value 4. In the
mini-max search, the minimizing and maximazing agents are choosing their moves based on expected values given
the known 10%-90% distribution of 2-tiles and 4-tiles.

http://kristianmschmidt.pythonanywhere.com/twentyfortyeight

I originally made a version of the backend to this project as an assignment to the online 'micro-master in Artificial intelligence' at Columbia University. Since then I've fine-tuned the algorithms, added expected-value considerations, designed a responsive front-end and put it all together using Flask. 
