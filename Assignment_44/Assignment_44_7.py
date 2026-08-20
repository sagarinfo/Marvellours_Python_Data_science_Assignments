import pandas as pd
import matplotlib.pyplot as plt

def plot_bar_chart(df):
    df_copy = df.copy()
    if 'Total' not in df_copy.columns:
        df_copy['Total'] = df_copy['Math'] + df_copy['Science'] + df_copy['English']
    print("--- Bar Plot Generation ---")
    plt.figure(figsize=(6, 4))
    plt.bar(df_copy['Name'], df_copy['Total'], color='skyblue')
    plt.xlabel('Student Name')
    plt.ylabel('Total Marks')
    plt.title('Student Names vs Total Marks')
    plt.show()

def main():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(data)
    plot_bar_chart(df)

if __name__ == "__main__":
    main()