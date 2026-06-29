def main():
    No = int(input("Enter a number: "))
    print("The factors of", No, "are:")
    for i in range(1, No + 1):
        if No % i == 0:
            print(i)
if __name__ == "__main__":
    main()            