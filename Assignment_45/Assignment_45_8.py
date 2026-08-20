import pandas as pd
import matplotlib.pyplot as plt

def generate_histogram(df):
    print("--- Histogram Generation ---")
    plt.figure(figsize=(6, 4))
    plt.hist(df['Math'], bins=3, color='purple', edgecolor='black', alpha=0.7)
    plt.xlabel('Math Marks')
    plt.ylabel('Frequency')
    plt.title('Histogram of Math Marks')
    plt.show()

def main():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(data)
    generate_histogram(df)

if __name__ == "__main__":
    main()