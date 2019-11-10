from common.constants import face, faces

def highcard(hand):
    allfaces = [f for f,s in hand]
    return 'highcard'