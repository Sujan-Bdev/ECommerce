import csv
from math import sqrt
import numpy as np
import pandas as pd

path = "./ml-100k/u.data"
df = pd.read_csv(path, sep='\t')
df.columns
Index([u'UserID', u'ItemId', u'Rating', u'Timestamp'], dtype='object')

print(df.shape(100000, 4))

