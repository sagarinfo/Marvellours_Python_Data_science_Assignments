import pandas as pd

def count_passed_students(df):
    df_copy = df.copy()
    df_copy['Total'] = df_copy['Math'] + df_copy['Science'] + df_copy['English']
    df_copy['Status'] = df_copy['Total'].apply(lambda x: 'Pass' if x >= 250 else 'Fail')
    pass_count = (df_copy['Status'] == 'Pass').sum()
    print("--- Passed Students Count Output ---")
    print(f"Number of students passed: {pass_count}")

def main():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(data)
    count_passed_students(df)

if __name__ == "__main__":
    main()