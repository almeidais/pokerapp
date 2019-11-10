from common.constants import face, faces

def royalflush(hand):
    f = face
    fs = 'T J Q K A'
    ordered = sorted(hand, key=lambda card: (f.index(card.face), card.suit))
    first, rest = ordered[0], ordered[1:]
    if ( all(card.suit == first.suit for card in rest) and
         ' '.join(card.face for card in ordered) in fs ):
        return 'royalflush'
    return False