
def main():
    
    filename = input("Enter a File name : ")
    word = input("Enter word to search : ")
    try:
        fobj = open(filename,"r")
        
        found = False
        for line in fobj:
            words=line.split()
            for w in words:
                if w == word:
                    found = True
                    break
            if found:
                break    
                     
        fobj.close()
        
        if found:
            print("word found")
        else:
            print("word not found")    
        
    except FileNotFoundError as Fobj:
        print("File is not present in current Directory")
        

if __name__ == "__main__":
    main()