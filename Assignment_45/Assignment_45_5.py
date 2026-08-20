import pandas as pd

def append_status_column(df):
    df_copy = df.copy()
    df_copy['Total'] = df_copy['Math'] + df_copy['Science'] + df_copy['English']
    df_copy['Status'] = df_copy['Total'].apply(lambda x: 'Pass' if x >= 250 else 'Fail')
    print("--- Status Column Output ---")
    print(df_copy[['Name', 'Total', 'Status']])
    return df_copy

def main():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(data)
    append_status_column(df)

if __name__ == "__main__":
    main()