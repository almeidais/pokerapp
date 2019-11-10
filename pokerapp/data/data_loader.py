# Loads the file in TXT format
def data_loader(src):
    player1 = []
    player2 = []

    with open(src, 'r') as f:
        data = f.read().splitlines()
    return data