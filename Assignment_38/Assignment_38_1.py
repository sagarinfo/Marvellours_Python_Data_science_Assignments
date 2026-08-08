import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_dataset():
    df = pd.read_csv("student_performance_ml.csv")
    return df


def display_dataset_information(df):

    print("\nFirst 5 Records:")
    print(df.head())

    print("\nLast 5 Records:")
    print(df.tail())

    print("\nTotal Rows and Columns:")
    print(df.shape)

    print("\nColumn Names:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)




def main():

    df = load_dataset()

    display_dataset_information(df)
if __name__ == "__main__":
    main()