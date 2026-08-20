import pandas as pd

def sort_by_total(df):
    df_copy = df.copy()
    if 'Total' not in df_copy.columns:
        df_copy['Total'] = df_copy['Math'] + df_copy['Science'] + df_copy['English']
    sorted_df = df_copy.sort_values(by='Total', ascending=False)
    print("--- Sorted DataFrame by Total ---")
    print(sorted_df)

def main():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(data)
    sort_by_total(df)

if __name__ == "__main__":
    main()