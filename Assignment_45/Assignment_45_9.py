import pandas as pd

def rename_math_column(df):
    df_copy = df.copy()
    df_copy = df_copy.rename(columns={'Math': 'Mathematics'})
    print("--- Column Rename Output ---")
    print(df_copy)

def main():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(data)
    rename_math_column(df)

if __name__ == "__main__":
    main()