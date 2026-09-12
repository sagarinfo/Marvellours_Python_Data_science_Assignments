def determine_confusion_matrix_values(actual, predicted):
    """Manually calculates TP, TN, FP, FN counts."""
    tp = tn = fp = fn = 0
    
    for a, p in zip(actual, predicted):
        if a == 1 and p == 1:
            tp += 1
        elif a == 0 and p == 0:
            tn += 1
        elif a == 0 and p == 1:
            fp += 1
        elif a == 1 and p == 0:
            fn += 1
            
    return tp, tn, fp, fn

def main():
    actual = [1, 1, 1, 1, 0, 0, 0, 0]
    predicted = [1, 1, 0, 1, 0, 1, 0, 0]
    
    tp, tn, fp, fn = determine_confusion_matrix_values(actual, predicted)
    
    print(f"True Positive (TP)  = {tp}")
    print(f"True Negative (TN)  = {tn}")
    print(f"False Positive (FP) = {fp}")
    print(f"False Negative (FN) = {fn}")

if __name__ == "__main__":
    main()