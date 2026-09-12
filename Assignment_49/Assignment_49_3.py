from sklearn.preprocessing import StandardScaler

def scale_features(data):
    """Performs feature scaling using StandardScaler."""
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    return scaled_data

def main():
    dataset = [[25, 20000],
               [30, 40000],
               [35, 80000]]
    
    scaled_dataset = scale_features(dataset)
    print("Scaled Dataset:")
    print(scaled_dataset)

if __name__ == "__main__":
    main()