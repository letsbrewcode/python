# ScoreBoard
# Design a scoreboard to track the scores of players in a game
# Scoreboard should support 3 functions
# 1. add_score:
# Accept a player name and score. If playerId already exists then
# add the score to the existing score.
# 2. top:
# Accepts nothing. Return the top player in the ScoreBoard.
# 3. reset: 
# Accepts the playerId and reset the score to 0. It will be
# Gauranteed that player will exist in ScoreBoard.
# 

class ScoreBoard:
    def __init__(self):
        # Complete the init.

    # Add methods to support the calls below

if __name__ == '__main__':
    s = ScoreBoard()
    s.add_score('A',85)
    s.add_score('B',63)
    s.add_score('C',44)
    s.add_score('D',51)
    s.add_score('E',5)
    print(s.top())
    s.reset('A')
    s.reset('B')
    s.add_score('B',51)
    print(s.top())
    s.add_score('E',90)
    print(s.top())
