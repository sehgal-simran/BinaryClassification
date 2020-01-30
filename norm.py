import pandas as pd
import scipy
from sklearn.preprocessing import StandardScaler
import numpy

x = pd.read_csv("HTRU_2.csv")
scaler = StandardScaler()
X_new = scaler.fit_transform(x)

numpy.savetxt("norm.csv", X_new,delimiter = "," )
