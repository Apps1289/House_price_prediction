import pandas as pd
from sklearn.model_selection import train_test_split
from data_preprocessing import preprocess

df = pd.read_csv("..\\Data\\cleaned_heart_disease_data.csv")
X = df.drop('heart_disease', axis=1)
y = df['heart_disease']

#split the dataset into training(80%), testing(10%) and validation set(10%)


X_train, X_temp, y_train, y_temp = train_test_split(
    X, y, test_size=0.2, random_state=42,stratify=y
    )

#split the temporary set into testing and validation sets
X_test, X_val, y_test, y_val = train_test_split(
    X_temp, y_temp, test_size=0.5, random_state=42,stratify=y_temp
    )

preprocessor = preprocess()
X_train = preprocessor.fit_transform(X_train)
X_test = preprocessor.transform(X_test)
X_val = preprocessor.transform(X_val)


