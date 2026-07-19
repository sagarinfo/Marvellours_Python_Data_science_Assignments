
def main():
    filename = input("Enter a File name : ")
    try:
        fobj = open(filename,"r")
        print("File gets Opened")
        
        count=0
        for line in fobj:
           print(line,end="")
        fobj.close()
        
    except FileNotFoundError as Fobj:
        print("File is not present in current Directory")
        

if __name__ == "__main__":
    main()