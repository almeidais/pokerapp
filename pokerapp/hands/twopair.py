from common.constants import face, faces

def twopair(hand):
    allfaces = [f for f,s in hand]
    allftypes = set(allfaces)
    pairs = [f for f in allftypes if allfaces.count(f) == 2]
    if len(pairs) != 2:
        return False
    p0, p1 = pairs
    other = [(allftypes - set(pairs)).pop()]
    return 'twopair'