import pandas as pd
import matplotlib.pyplot as plt

def plot_line_chart(df):
    print("--- Line Chart Generation ---")
    amit_row = df[df['Name'] == 'Amit']
    subjects = ['Math', 'Science', 'English']
    marks = amit_row[subjects].values.flatten()
    
    plt.figure(figsize=(6, 4))
    plt.plot(subjects, marks, marker='o', color='green', linestyle='-')
    plt.xlabel('Subjects')
    plt.ylabel('Marks')
    plt.title("Amit's Marks Across Subjects")
    plt.grid(True)
    plt.show()

def main():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(data)
    plot_line_chart(df)

if __name__ == "__main__":
    main()