import pandas as pd
import numpy as np

class KNNClassifier:
    def __init__(self, dataset):
        self.df = pd.DataFrame(dataset, columns=['Study Hours', 'Attendance', 'Result'])

    def predict(self, new_point, k=3):
        X_train = self.df[['Study Hours', 'Attendance']].to_numpy()
        labels = self.df['Result'].to_numpy()

        distances = np.sqrt(np.sum((X_train - new_point) ** 2, axis=1))

        result_df = pd.DataFrame({
            'Distance': distances,
            'Result': labels
        })

        result_df = result_df.sort_values(by='Distance').reset_index(drop=True)
        k_nearest = result_df.head(k)
        predicted_result = k_nearest['Result'].mode()[0]

        return predicted_result


def main():
    # Dataset from Assignment 3 description
    dataset = [
        [2, 60, 'Fail'],
        [5, 80, 'Pass'],
        [6, 85, 'Pass'],
        [1, 50, 'Fail']
    ]

    knn = KNNClassifier(dataset)

    # Accept user input for Study Hours and Attendance
    study_hours = float(input("Enter Study Hours: "))
    attendance = float(input("Enter Attendance: "))
    new_point = np.array([study_hours, attendance])

    k = 3
    predicted_result = knn.predict(new_point, k=k)

    print(f"\nPredicted Result: {predicted_result}")


if __name__ == "__main__":
    main()