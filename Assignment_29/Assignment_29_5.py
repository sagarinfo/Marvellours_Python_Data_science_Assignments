import sys

def Frequency(filename, word):
    try:
        file = open(filename, "r")

        data = file.read()
        file.close()

        words = data.split()

        count = 0
        for i in words:
            if i == word:
                count += 1

        print(word, "appears", count, "times in", filename)

    except FileNotFoundError:
        print("File does not exist.")

def main():
    if len(sys.argv) != 3:
        print("Usage: python Frequency.py <filename> <word>")
        return

    Frequency(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()