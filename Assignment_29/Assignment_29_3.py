import sys

def CopyFile(filename):
    try:
        source = open(filename, "r")
        destination = open("demo.txt", "w")

        data = source.read()
        destination.write(data)

        source.close()
        destination.close()

        print("Contents copied successfully into Demo.txt")

    except FileNotFoundError:
        print("File does not exist.")

def main():
    if len(sys.argv) != 2:
        print("")
        return

    CopyFile(sys.argv[1])

if __name__ == "__main__":
    main()