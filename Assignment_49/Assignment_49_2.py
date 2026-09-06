import numpy as np

def calculate_variance_std(data):
    """Calculates the variance and standard deviation of a dataset using NumPy."""
    # Using ddof=0 for population variance/std (default standard behavior)
    variance_val = np.var(data)
    std_val = np.std(data)
    return variance_val, std_val

def main():
    dataset = [6, 7, 8, 9, 10, 11, 12]
    variance_val, std_val = calculate_variance_std(dataset)
    print(f"Variance = {variance_val}")
    print(f"Standard Deviation = {std_val}")

if __name__ == "__main__":
    main()