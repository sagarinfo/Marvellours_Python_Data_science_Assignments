import pandas as pd

def export_dataframe_to_csv(df):
    df_copy = df.copy()
    df_copy['Total'] = df_copy['Math'] + df_copy['Science'] + df_copy['English']
    df_copy['Status'] = df_copy['Total'].apply(lambda x: 'Pass' if x >= 250 else 'Fail')
    file_name = 'student_final_results.csv'
    df_copy.to_csv(file_name, index=False)
    print("--- CSV Export Output ---")
    print(f"DataFrame successfully exported to {file_name}")

def main():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(data)
    export_dataframe_to_csv(df)

if __name__ == "__main__":
    main()