from sklearn.metrics import classification_report

def generate_report(actual, predicted):
    """Generates a text summary of the classification report using scikit-learn."""
    return classification_report(actual, predicted)

def main():
    actual = [1, 1, 1, 1, 0, 0, 0, 0]
    predicted = [1, 1, 0, 1, 0, 1, 0, 0]
    
    report = generate_report(actual, predicted)
    print("Classification Report:")
    print(report)

if __name__ == "__main__":
    main()