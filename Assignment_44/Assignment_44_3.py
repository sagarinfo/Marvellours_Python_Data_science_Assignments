import pandas as pd

def add_total_marks(df):
    df_copy = df.copy()
    df_copy['Total'] = df_copy['Math'] + df_copy['Science'] + df_copy['English']
    print("--- Total Marks Added ---")
    print(df_copy)
    return df_copy

def main():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(data)
    add_total_marks(df)

if __name__ == "__main__":
    main()