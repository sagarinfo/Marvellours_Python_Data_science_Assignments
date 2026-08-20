import pandas as pd
import numpy as np

def fill_missing_values():
    data2 = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [np.nan, 76, 88],
        'Science': [91, np.nan, 85]
    }
    df2 = pd.DataFrame(data2)
    print("--- Original DataFrame with Missing Values ---")
    print(df2)
    
    df2['Math'] = df2['Math'].fillna(df2['Math'].mean())
    df2['Science'] = df2['Science'].fillna(df2['Science'].mean())
    
    print("\n--- DataFrame After Filling Missing Values ---")
    print(df2)

def main():
    fill_missing_values()

if __name__ == "__main__":
    main()