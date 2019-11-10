from common.card import Card

def prepare_hand(cards):
   
    hand = []
    for card in cards.split():
        f, s = card[:-1], card[-1]
        hand.append(Card(f, s))
    return hand