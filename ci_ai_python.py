import logging

import pandas as pd

if (__name__ == "__main__"):
    logging.basicConfig(format='[%(asctime)s] %(levelname)s::%(module)s::%(funcName)s() %(message)s', level=logging.DEBUG)

logging.info("Importing the data from the given training dataset")
data = pd.read_csv('Training_Dataset_1.csv')

