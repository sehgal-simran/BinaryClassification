import pandas as pd
from sklearn.model_selection import train_test_split

dataset = "norm.csv"
data = pd.read_csv(dataset)
X_train, X_test = train_test_split(data,test_size = 0.2)
X_train.to_csv("train_norm.csv", header =False, index = False)
X_test.to_csv("test_norm.csv", header = False, index = False)
