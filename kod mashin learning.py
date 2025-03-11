
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv('car_data.csv')

label_encoder_nam = LabelEncoder()
label_encoder_karkard = LabelEncoder()
label_encoder_az = LabelEncoder()
label_encoder_gheimat = LabelEncoder()
data['nam'] = label_encoder_nam.fit_transform(data['nam'])
data['karkard'] = label_encoder_az.fit_transform(data['karkard'])
data['az'] = label_encoder_az.fit_transform(data['az'])
data['gheimat'] = label_encoder_az.fit_transform(data['gheimat'])

X = data[['nam','karkard','az']]
y = data['gheimat']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

def takhmin(nam, karkard, az):
    nam_encoded = label_encoder_nam.transform([nam])[0]
    karkard_numeric = float(karkard.replace(',', '').replace(' کیلومتر', ''))
    az_encoded = label_encoder_az.transform([az])[0]
    return model.predict([[nam_encoded, karkard_numeric, az_encoded]])

predicted_price = takhmin('پراید 131، مدل 1389', '220,000 کیلومتر', 'تهران')
print(f'Predicted Price: {predicted_price}')


#2020, 15000, 'Toyota', 'Corolla'