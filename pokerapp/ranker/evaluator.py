from ranker.rank import rank

rankorder = ['royalflush', 'straightflush', 'fourofakind', 'fullhouse',
                  'flush', 'straight', 'threeofakind',
                  'twopair', 'onepair', 'highcard']

def evaluator(data):
    wins_player1 = 0 
    wins_player2 = 0 
    for line in data:
        player1 = rank(line[0:14])
        player2 = rank(line[15:29])
        if rankorder.index(player1) < rankorder.index(player2):
            wins_player1 += 1
        else: 
            wins_player2 += 1

    return 'Player 1 has won ' + str(wins_player1) + ' hands out of ' + str(len(data)) + '. Therefore, Player 2 has won ' + str(wins_player2) + '.'