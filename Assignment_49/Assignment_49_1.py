import numpy as np

def calculate_mean(data):
    """Calculates the mean of a dataset using NumPy."""
    return np.mean(data)

def main():
    dataset = [6, 7, 8, 9, 10, 11, 12]
    mean_val = calculate_mean(dataset)
    print(f"Mean of the dataset = {mean_val}")

if __name__ == "__main__":
    main()