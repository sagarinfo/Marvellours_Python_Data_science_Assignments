def main():
    try:
        filename = input("Enter a File name : ")
        fobj = open(filename,"r")
        print("File gets Opened")
        
        data = fobj.read()
        
        print(data)
        fobj.close()
        
    except FileNotFoundError as Fobj:
        print("File is not present in current Directory")
        

if __name__ == "__main__":
    main()