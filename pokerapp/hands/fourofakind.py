def fourofakind(hand):
    allfaces = [f for f,s in hand]
    allftypes = set(allfaces)
    if len(allftypes) != 2:
        return False
    for f in allftypes:
        if allfaces.count(f) == 4:
            allftypes.remove(f)
            return 'fourofakind'
    else:
        return False