import pandas as pd

def compute_statistics(df):
    print("--- Descriptive Statistics ---")
    print(df.describe())

def main():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(data)
    compute_statistics(df)

if __name__ == "__main__":
    main()