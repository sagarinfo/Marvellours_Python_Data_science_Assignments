import pandas as pd

def drop_column(df):
    print("--- DataFrame After Dropping English Column ---")
    df_dropped = df.drop(columns=['English'])
    print(df_dropped)

def main():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(data)
    drop_column(df)

if __name__ == "__main__":
    main()