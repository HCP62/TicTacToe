# TicTacToe
This is a repo for the 2 TicTacToe projects I have made. You can also find them in my python repo and java repo

This tictactoe is  the same game, but in 2 languages, both using the same algorithm.

The algorithm used to make the Unbeatable TicTacToe is the Minimax algorithm. All sources for which I used are linked at the bottom of my Python program.

Essentially what is going on is that the computer will test each move it makes in conjuction with what move you could potentially make next, until it finds the move best suited for itself, and the move that is least benefitial for you.

With the java file, it is just Minimax TicTacToe, plain and simple. With the python file, I've placed in options to play against a computer that chooses it's placement at random dubbed "Easy", an AI that prioritizes certain placements (blocking you, starting at a certain place, etc) dubbed "Medium", and as "Hard" I have the Minimax AI, which even in my own testing playing against I was only able to draw. I ran these AIs against one another (using method AITest()), and here are the results:

R = Random placement computer
P = AI that has certain priorities
M = Minimax AI

R vs P:
  (R: ~200 |
  P: ~700
  Ties: ~100)
P vs M:
  (P: 0 |
  M: 0
  Ties: 100)
R vs M:
  (R: 0 |
  M: 1000
  Ties: 0)
  
What really surprised me was the fact that even though one AI is more advanced than the other, it still is unable to beat the other. I thought that Minimax would win by a landslide over it, so I was really taken aback and was proud of the fact that even an AI that has only a few priorities (to block, to go for a winning play, etc.) is able to match up with an AI that tests each move and picks out the most benefitial one for itself.
