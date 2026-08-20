import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def process_student_data():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(data)
    print("--- Basic Information ---")
    print("DataFrame:")
    print(df)
    print(f"\nShape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
    print("\nData Types:")
    print(df.dtypes)
    return df

def main():
    df = process_student_data()

if __name__ == "__main__":
    main()