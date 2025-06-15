import os
import pandas as pd
import numpy as np

def load_titanic_csv():
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/titanic.csv'))
    return pd.read_csv(path)
