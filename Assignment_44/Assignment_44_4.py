import pandas as pd

def filter_science_marks(df):
    print("--- Filtered Science Marks (> 85) ---")
    filtered_df = df[df['Science'] > 85]
    print(filtered_df)

def main():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(data)
    filter_science_marks(df)

if __name__ == "__main__":
    main()