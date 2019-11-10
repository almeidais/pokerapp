from common.constants import face, faces

def straightflush(hand):
    f,fs = (face, faces)
    ordered = sorted(hand, key=lambda card: (f.index(card.face), card.suit))
    first, rest = ordered[0], ordered[1:]
    if ( all(card.suit == first.suit for card in rest) and
         ' '.join(card.face for card in ordered) in fs ):
        return 'straightflush'
    return False