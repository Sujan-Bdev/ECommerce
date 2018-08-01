import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split

path = "./ml-100k/u.data"
df = pd.read_csv(path, sep="\t")
df.columns = pd.Index([u'UserID', u'ItemId', u'Rating', u'Timestamp'], dtype='object')
df.groupby(['Rating'])['UserID'].count()
plt.hist(df['Rating'])

n_users = df.UserID.unique().shape[0]
n_items = df.ItemId.unique().shape[0]
print(str(n_users) + ' users')
print(str(n_items) + ' movies')

ratings = np.zeros((n_users, n_items))
for row in df.itertuples():
    ratings[row[1] - 1, row[2] - 1] = row[3]

sparsity = float(len(ratings.nonzero()[0]))
sparsity /= (ratings.shape[0]*ratings.shape[1])
sparsity *=100
print('Sparsity: {:4.2f}%'.format(sparsity))

ratings_train, ratings_test = train_test_split(ratings, test_size=0.33, random_state=42)
print(ratings_train.shape(631,	1682))
