import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

#data = pd.read_csv('processed_data_final12.csv')
data_new = pd.read_csv('processed_data_final12.csv', encoding='latin-1')
data_new.columns = ['Seq', 'Offset', 'sTtl', 'sMeanPktSz', 'tcp', 'AckDat', 'RST', 'INT', 'TcpRtt', 'icmp']

data_new.isnull().sum()

data_new= data_new.fillna(0)


import pickle

filename = 'finalized_model1.sav'  # Make sure this is the correct filename

# Load the model from the file
loaded_model = pickle.load(open(filename, 'rb'))
y_pred = loaded_model.predict(data_new)
print(y_pred)