from common.constants import DATA_SOURCE
from data.data_loader import data_loader
from ranker.evaluator import evaluator

def run():
    data = data_loader(DATA_SOURCE)
    result = evaluator(data)
    print(result)