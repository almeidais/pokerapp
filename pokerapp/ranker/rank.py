from hands import * 
from data.prepare_hand import prepare_hand

rankorder =  (royalflush, straightflush, fourofakind, fullhouse,
                  flush, straight, threeofakind,
                  twopair, onepair, highcard)

def rank(cards):
    hand = prepare_hand(cards)
    for rnk in rankorder:
        rank = rnk(hand)
        if rank:
            break
    return rank