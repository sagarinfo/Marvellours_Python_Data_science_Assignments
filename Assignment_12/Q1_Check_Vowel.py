def main():
    name = input("Enter a character: ")
    if name.lower() in ['a', 'e', 'i', 'o', 'u']:
        print(name, "is a vowel.")
    else:
        print(name, "is not a vowel.")  
if __name__ == "__main__":
    main()        