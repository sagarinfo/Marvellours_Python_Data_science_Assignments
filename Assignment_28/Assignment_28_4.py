
def main():
    
    file1 = input("Enter a first File name : ")
    file2 = input("Enter a second File name : ")
    try:
        fobj1 = open(file1,"r")
        fobj2 = open(file2,"w")
        
        
        print("File gets Opened")
        
        
        for line in fobj1:
            fobj2.write(line)
        fobj1.close()
        fobj2.close()
        
    except FileNotFoundError as Fobj:
        print("File is not present in current Directory")
        

if __name__ == "__main__":
    main()