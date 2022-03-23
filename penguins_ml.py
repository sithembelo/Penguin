import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

penguin_df = pd.read_csv('streamlit_apps\penguin_ml\penguins.csv')
#print(penguin_df.head())

penguin_df.dropna(inplace=True)
output = penguin_df['species']
features = penguin_df[['island', 'bill_length_mm', 'bill_depth_mm','flipper_length_mm', 'body_mass_g', 'sex']]
features = pd.get_dummies(features)
output, uniques = pd.factorize(output)

x_train, x_test, y_train, y_test = train_test_split(features, output, test_size=.8)
rfc = RandomForestClassifier(random_state=15)
rfc.fit(x_train, y_train)
y_pred = rfc.predict(x_test)
score = accuracy_score(y_pred, y_test)
print('Our accuracy score for this model is {}'.format(score))

rf_pickle = open('streamlit_apps\penguin_app\penguin_ml\random_forest_penguin.pkl', 'wb')
pickle.dump(rfc, rf_pickle)
rf_pickle.close()
output_pickle = open('streamlit_apps\penguin_app\penguin_ml\output_penguin.pkl', 'wb')
pickle.dump(uniques, output_pickle)
output_pickle.close()