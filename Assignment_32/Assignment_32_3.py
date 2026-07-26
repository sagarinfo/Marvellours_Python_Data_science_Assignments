import time

def main():

    filename = input("Enter file name : ")

    while True:

        try:

            file = open(filename, "r")

            data = file.read()

            if data == "":
                print("File is empty.")
            else:
                print("\nFile Contents")
                print("---------------------")
                print(data)

            file.close()

        except FileNotFoundError:
            print("Error : File does not exist.")

        except PermissionError:
            print("Error : Permission denied.")

        except OSError:
            print("Error : File cannot be opened.")

        time.sleep(60)

if __name__ == "__main__":
    main()