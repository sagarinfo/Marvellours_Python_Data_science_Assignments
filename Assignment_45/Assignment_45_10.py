import pandas as pd
import matplotlib.pyplot as plt

def generate_boxplot(df):
    print("--- Boxplot Generation ---")
    plt.figure(figsize=(5, 4))
    plt.boxplot(df['English'], patch_artist=True, boxprops=dict(facecolor='lightblue'))
    plt.ylabel('Marks')
    plt.title('Boxplot for English Marks')
    plt.show()

def main():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(data)
    generate_boxplot(df)

if __name__ == "__main__":
    main()