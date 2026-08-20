import pandas as pd

def calculate_average_by_gender(df):
    df_copy = df.copy()
    df_copy['Gender'] = ['Male', 'Male', 'Female']
    avg_marks = df_copy.groupby('Gender')[['Math', 'Science', 'English']].mean()
    print("--- Group By Gender Average Marks Output ---")
    print(avg_marks)

def main():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(data)
    calculate_average_by_gender(df)

if __name__ == "__main__":
    main()