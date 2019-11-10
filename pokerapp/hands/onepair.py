from common.constants import face, faces

def onepair(hand):
    allfaces = [f for f,s in hand]
    allftypes = set(allfaces)
    pairs = [f for f in allftypes if allfaces.count(f) == 2]
    if len(pairs) != 1:
        return False
    allftypes.remove(pairs[0])
    return 'onepair'