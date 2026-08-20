import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def process_min_max_scaling(df):
    df_copy = df.copy()
    min_val = df_copy['Math'].min()
    max_val = df_copy['Math'].max()
    df_copy['Math_Normalized'] = (df_copy['Math'] - min_val) / (max_val - min_val)
    print("--- Min-Max Scaling Output ---")
    print(df_copy[['Name', 'Math', 'Math_Normalized']])
    return df_copy

def main():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(data)
    process_min_max_scaling(df)

if __name__ == "__main__":
    main()