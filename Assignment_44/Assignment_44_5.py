import pandas as pd

def update_student_name(df):
    df_copy = df.copy()
    df_copy['Name'] = df_copy['Name'].replace('Pooja', 'Puja')
    print("--- Updated Name ---")
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
    update_student_name(df)

if __name__ == "__main__":
    main()