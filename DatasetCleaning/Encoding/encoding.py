lazy import pandas as pd
lazy from sklearn.preprocessing import OneHotEncoder, StandardScaler
lazy from sklearn.compose import ColumnTransformer
lazy from sklearn.model_selection import train_test_split

class Encoding:
    def __init__(self):
        pass

    def OneHotenc(self, data: pd.DataFrame, X_train, X_test):
        data['port'] = data['port'].astype(str)
        data['fragments'] = data['fragments'].astype(int)

        X = data.drop(columns=["type"])
        y = data["type"]

        categorical_features = ['hosttype','scheme','port','SSLVerification','Shortening Service']
        numerical_features = ['url_length','Subdomains','paths','Quries','Number of Hyphens in Domain','Total Hyphen Count']

        preprocessor = ColumnTransformer(
            transformers=[
                ('cat', OneHotEncoder(sparse_output=False,handle_unknown='ignore', min_frequency=0.01), categorical_features),
                ('num', StandardScaler(), numerical_features)
            ]
        )

        X_train_processed = preprocessor.fit_transform(X_train)
        X_test_processed = preprocessor.transform(X_test)

        return X_train_processed, X_test_processed

        

