from collections import namedtuple

class Card(namedtuple('Card', 'face, suit')):
    def __repr__(self):
        return ''.join(self)