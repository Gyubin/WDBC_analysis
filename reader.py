import pandas as pd
import numpy as np

class Reader(object):
    def __init__(self):
        data = pd.read_csv('_data/wdbc.data', header=-1) # No header in the file
        y = np.array(data[1])
        y[y == 'M'] = 1
        y[y == 'B'] = 0
        self.y = y.astype('int32')
        self.data_id = np.array(data[0])
        self.X = np.array(data.iloc[:, 2:])
    
    def get_entire_data(self):
        return self.X, self.y, self.data_id