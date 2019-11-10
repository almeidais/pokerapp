from common.constants import face, faces

def straight(hand):
    f,fs = (face, faces)
    ordered = sorted(hand, key=lambda card: (f.index(card.face), card.suit))
    first, rest = ordered[0], ordered[1:]
    if ' '.join(card.face for card in ordered) in fs:
        return 'straight'
    return False