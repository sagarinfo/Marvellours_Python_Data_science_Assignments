import pandas as pd
import numpy as np

class KNNClassifier:
    def __init__(self, dataset):
        # Convert dataset to a pandas DataFrame for structured manipulation
        self.df = pd.DataFrame.from_dict(dataset, orient='index', columns=['X', 'Y', 'Label'])

    def predict(self, new_point, k=3):
        # Extract X and Y coordinates as numpy arrays
        X_train = self.df[['X', 'Y']].to_numpy()
        labels = self.df['Label'].to_numpy()
        point_names = self.df.index.to_numpy()

        # Calculate Euclidean distance using NumPy vectorization
        distances = np.sqrt(np.sum((X_train - new_point) ** 2, axis=1))

        # Combine point names, distances, and labels into a structured array/DataFrame
        result_df = pd.DataFrame({
            'Name': point_names,
            'Distance': distances,
            'Label': labels
        })

        # Sort distances in ascending order
        result_df = result_df.sort_values(by='Distance').reset_index(drop=True)

        # Select K nearest neighbors
        k_nearest = result_df.head(k)

        # Predict the class based on majority voting
        predicted_class = k_nearest['Label'].mode()[0]

        return k_nearest, predicted_class


def main():
    # Dataset from the problem description
    dataset = {
        'A': [1, 2, 'Red'],
        'B': [2, 3, 'Red'],
        'C': [3, 1, 'Blue'],
        'D': [6, 5, 'Blue']
    }

    knn = KNNClassifier(dataset)

    # Accept X and Y coordinates from the user
    x = float(input("Enter X coordinate: "))
    y = float(input("Enter Y coordinate: "))
    new_point = np.array([x, y])

    k = 3
    nearest_neighbors, predicted_class = knn.predict(new_point, k=k)

    print("\nNearest Neighbors:")
    for _, row in nearest_neighbors.iterrows():
        print(f"{row['Name']} - Distance: {row['Distance']:.2f}")

    print(f"\nPredicted Class: {predicted_class}")


if __name__ == "__main__":
    main()