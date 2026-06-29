def main():
    Marks = int(input("Enter the marks: "))
    if Marks >= 75:
        print("Distinction")
    elif Marks >= 60:
        print("First Class")
    elif Marks >= 50:
        print("Second Class")
    else:
        print("Fail")
if __name__ == "__main__":
    main()