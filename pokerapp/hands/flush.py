from common.constants import face, faces

def flush(hand):
    allstypes = {s for f, s in hand}
    if len(allstypes) == 1:
        allfaces = [f for f,s in hand]
        return 'flush'
    return False