def Area_Of_Circle(radius,pi = 3.14159):
    area = pi * (radius ** 2)
    return area
def main():
    Radius = float(input("Enter the radius of the circle: "))
    area = Area_Of_Circle(Radius)
    print("The area of the circle is:", area)
if __name__ == "__main__":
    main()