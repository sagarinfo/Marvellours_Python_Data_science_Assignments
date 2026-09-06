def calculate_mean(values):
    """Calculates the mean of a list of numbers."""
    return sum(values) / len(values)

def calculate_slope_intercept(x, y):
    """Calculates the slope (m) and intercept (c) for simple linear regression."""
    mean_x = calculate_mean(x)
    mean_y = calculate_mean(y)
    
    numerator = 0
    denominator = 0
    
    for i in range(len(x)):
        numerator += (x[i] - mean_x) * (y[i] - mean_y)
        denominator += (x[i] - mean_x) ** 2
        
    m = numerator / denominator
    c = mean_y - (m * mean_x)
    
    return mean_x, mean_y, m, c

def main():
    # Dataset from the assignment specification
    X = [1, 2, 3, 4, 5]
    Y = [3, 4, 2, 4, 5]
    
    # Calculate components
    mean_x, mean_y, m, c = calculate_slope_intercept(X, Y)
    
    # Print expected outputs
    print(f"Mean of X = {mean_x}")
    print(f"Mean of Y = {mean_y}")
    print()
    print(f"Slope (m) = {m}")
    print(f"Intercept (c) = {c}")
    print()
    print(f"Regression Equation:")
    print(f"Y = {m}X + {c}")
    print()
    
    # Example prediction for X = 6
    x_test = 6
    predicted_y = (m * x_test) + c
    print(f"Predicted Y for X = {x_test} : {predicted_y}")

if __name__ == "__main__":
    main()