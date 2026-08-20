import pandas as pd
import numpy as np

class KNNClassifier:
    def __init__(self, dataset):
        self.df = pd.DataFrame.from_dict(dataset, orient='index', columns=['X', 'Y', 'Label'])

    def predict(self, new_point, k=3):
        X_train = self.df[['X', 'Y']].to_numpy()
        labels = self.df['Label'].to_numpy()
        point_names = self.df.index.to_numpy()

        distances = np.sqrt(np.sum((X_train - new_point) ** 2, axis=1))

        result_df = pd.DataFrame({
            'Name': point_names,
            'Distance': distances,
            'Label': labels
        })

        result_df = result_df.sort_values(by='Distance').reset_index(drop=True)
        k_nearest = result_df.head(k)
        predicted_class = k_nearest['Label'].mode()[0]

        return predicted_class


def main():
    dataset = {
        'A': [1, 2, 'Red'],
        'B': [2, 3, 'Red'],
        'C': [3, 1, 'Blue'],
        'D': [6, 5, 'Blue']
    }

    knn = KNNClassifier(dataset)

    x = float(input("Enter X coordinate: "))
    y = float(input("Enter Y coordinate: "))
    new_point = np.array([x, y])

    k_values = [1, 3, 5]
    
    print("\nPrediction Results")
    for k in k_values:
        predicted_class = knn.predict(new_point, k=k)
        print(f"K = {k} -> {predicted_class}")


if __name__ == "__main__":
    main()