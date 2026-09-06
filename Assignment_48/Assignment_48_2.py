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
    
    return m, c

def evaluate_model(x, y, m, c):
    """Calculates predicted Y values, Mean Squared Error (MSE), and R^2 Score."""
    y_pred = [(m * xi) + c for xi in x]
    mean_y = calculate_mean(y)
    
    mse = sum((y[i] - y_pred[i]) ** 2 for i in range(len(y))) / len(y)
    
    ss_total = sum((yi - mean_y) ** 2 for yi in y)
    ss_residual = sum((y[i] - y_pred[i]) ** 2 for i in range(len(y)))
    r2_score = 1 - (ss_residual / ss_total)
    
    return y_pred, mse, r2_score

def main():
    # Dataset from the previous question (Task 2 context)
    X = [1, 2, 3, 4, 5]
    Y = [3, 4, 2, 4, 5]
    
    # Calculate model parameters
    m, c = calculate_slope_intercept(X, Y)
    
    # Evaluate model performance
    y_pred, mse, r2 = evaluate_model(X, Y, m, c)
    
    print("--- Task 2: Model Performance Evaluation ---")
    print(f"Regression Equation: Y = {m}X + {c}")
    print("\n1. Predicted Y values using regression equation:")
    for xi, yi, ypi in zip(X, Y, y_pred):
        print(f"   For X = {xi}, Actual Y = {yi}, Predicted Y = {ypi:.2f}")
        
    print("\n2. Intermediate Calculations & Metrics:")
    print(f"   Mean Squared Error (MSE) = {mse:.4f}")
    print(f"   R^2 Score = {r2:.4f}")
    
    # Task 3: New dataset for salary prediction and plotting with matplotlib
    print("\n--- Task 3: Salary Prediction & Plotting ---")
    experience = [1, 2, 3, 4, 5]
    salary = [20000, 25000, 30000, 35000, 40000]
    
    m_sal, c_sal = calculate_slope_intercept(experience, salary)
    
    # Predict salary for 6 years of experience
    exp_test = 6
    predicted_salary = (m_sal * exp_test) + c_sal
    print(f"Predicted Salary for 6 Years Experience: ₹{int(predicted_salary)}")
    
    # Optional: Plotting using matplotlib (Task 3.3)
    try:
        import matplotlib.pyplot as plt
        
        # Data points
        plt.scatter(experience, salary, color='blue', label='Data points')
        
        # Regression line
        sal_pred = [(m_sal * ex) + c_sal for ex in experience]
        # Include test point for a complete visualization line
        full_exp = experience + [exp_test]
        full_sal_pred = [(m_sal * ex) + c_sal for ex in full_exp]
        
        plt.plot(full_exp, full_sal_pred, color='red', label='Regression line')
        plt.xlabel('Experience (Years)')
        plt.ylabel('Salary (₹)')
        plt.title('Experience vs Salary Linear Regression')
        plt.legend()
        plt.grid(True)
        plt.show()
    except ImportError:
        print("Matplotlib is not installed. Skipping plot generation.")

if __name__ == "__main__":
    main()