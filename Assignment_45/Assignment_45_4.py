import pandas as pd
import matplotlib.pyplot as plt

def generate_pie_chart(df):
    print("--- Pie Chart Generation ---")
    sagar_row = df[df['Name'] == 'Sagar']
    subjects = ['Math', 'Science', 'English']
    marks = sagar_row[subjects].values.flatten()
    
    plt.figure(figsize=(5, 5))
    plt.pie(marks, labels=subjects, autopct='%1.1f%%', startangle=140, colors=['gold', 'lightcoral', 'lightskyblue'])
    plt.title("Sagar's Subject Marks Distribution")
    plt.show()

def main():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(data)
    generate_pie_chart(df)

if __name__ == "__main__":
    main()