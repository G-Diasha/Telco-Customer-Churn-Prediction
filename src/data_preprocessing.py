import pandas as pd

path = 'c:\\Users\\User\\Desktop\\ML model\\dataset\\Telco_Cusomer_Churn.csv'

def load_data(path): # function to load and read the csv file
    df = pd.read_csv(path)
    return df

def encode_binary_columns(df): #function to convert the binary values to integer
    binary_cols= ['gender', 'Partner', 'Dependents','PhoneService', 'PaperlessBilling', 'Churn']
    mapping = {'Yes': 1, 'No': 0, 'Male' : 1, 'Female' : 0}
    df[binary_cols] = df[binary_cols].replace(mapping)
    return df


def encode_multi_column(df): #function to convert multicategorical column to boolean values with extra column creation
    multi_cols = [
        "MultipleLines", "InternetService", "OnlineSecurity",
        "OnlineBackup", "DeviceProtection", "TechSupport",
        "StreamingTV", "StreamingMovies", "Contract", "PaymentMethod"
    ]
    df = pd.get_dummies(df, columns=multi_cols, drop_first=True)
    return df

def numeric_columns(df):
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df = df.drop(columns= ['customerID'])
    bool_cols = df.select_dtypes(include = 'bool').columns
    df[bool_cols] = df[bool_cols].astype(int)
    return df

def preprocess_data(path: str):
    df = load_data(path)
    df = encode_binary_columns(df)
    df = encode_multi_column(df)
    df = numeric_columns(df)
    X = df.drop(columns = 'Churn')
    y= df['Churn']
    return X, y

