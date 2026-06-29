def calculate_area(length, width):
    area = length * width
    return area

def main():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    
    area = calculate_area(length, width)
    print("The area of the rectangle is:", area)
    
if __name__ == "__main__":
    main()