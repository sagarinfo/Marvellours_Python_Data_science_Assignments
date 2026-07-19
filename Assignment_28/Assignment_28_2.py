
def main():
    
    filename = input("Enter a File name : ")
    try:
        fobj = open(filename,"r")
        print("File gets Opened")
        
        count=0
        for line in fobj:
            words=line.split()
            count+=len(words)
            
        fobj.close()
        
        print("Total number of words in ",count)
    except FileNotFoundError as Fobj:
        print("File is not present in current Directory")
        

if __name__ == "__main__":
    main()