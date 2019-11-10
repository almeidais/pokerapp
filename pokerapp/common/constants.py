# All constant variables are declared here
import os

#Project root dir
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 

#Data source
DATA_SOURCE = os.path.join(ROOT_DIR, 'resources/poker.txt')

#List of available suits
suits = 'H S C D'
suit = suits.split()

#List of available faces
faces = '2 3 4 5 6 7 8 9 T J Q K A'
face = faces.split()