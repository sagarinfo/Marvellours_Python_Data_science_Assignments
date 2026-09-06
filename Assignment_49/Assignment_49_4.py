import numpy as np
from sklearn.preprocessing import StandardScaler

def calculate_euclidean_distances():
    """Calculates Euclidean distance between two points before and after scaling."""
    dataset = np.array([[25, 20000],
                        [30, 40000],
                        [35, 80000]])
    
    # Selecting two points (e.g., row 0 and row 1)
    point1_orig = dataset[0]
    point2_orig = dataset[1]
    
    # Distance before scaling
    dist_orig = np.linalg.norm(point1_orig - point2_orig)
    
    # Feature scaling
    scaler = StandardScaler()
    scaled_dataset = scaler.fit_transform(dataset)
    
    point1_scaled = scaled_dataset[0]
    point2_scaled = scaled_dataset[1]
    
    # Distance after scaling
    dist_scaled = np.linalg.norm(point1_scaled - point2_scaled)
    
    return dist_orig, dist_scaled

def main():
    d_orig, d_scaled = calculate_euclidean_distances()
    print(f"Euclidean Distance Before Scaling: {d_orig}")
    print(f"Euclidean Distance After Scaling: {d_scaled}")
    print("\nExplanation:")
    print("Before scaling, the distance is heavily dominated by features with larger numeric scales (like Salary spanning in tens of thousands), "
          "while smaller scales (like Age/Experience) are virtually ignored. After applying StandardScaler, all features are normalized to have a mean of 0 "
          "and standard deviation of 1, ensuring every feature contributes equally to the distance calculation.")

if __name__ == "__main__":
    main()