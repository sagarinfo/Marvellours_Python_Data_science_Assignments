import os

def main():
    filename = input("Enter a File name : ")
    if(os.path.exists(filename)):
        print("File is present in Current Directory")
    else:
        print("File is not Present")    

if __name__ == "__main__":
    main()