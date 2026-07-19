
def main():
    
    filename = input("Enter a File name : ")
    try:
        fobj = open(filename,"r")
        
        count=0
        for line in fobj:
            count+=1
            
        fobj.close()
        
        print("Total number of lines",count)
    except FileNotFoundError as Fobj:
        print("File is not present in current Directory")
        

if __name__ == "__main__":
    main()