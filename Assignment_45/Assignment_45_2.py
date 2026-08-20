import pandas as pd

def encode_gender_column(df):
    df_copy = df.copy()
    df_copy['Gender'] = ['Male', 'Male', 'Female']
    encoded_df = pd.get_dummies(df_copy, columns=['Gender'], prefix='Gender')
    print("--- One-Hot Encoding Output ---")
    print(encoded_df)
    return encoded_df

def main():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(data)
    encode_gender_column(df)

if __name__ == "__main__":
    main()