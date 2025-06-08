try:
    with open('sampfle.txt', 'r') as file:
        print("Reading file content:")

        i = 1
        for line in file:
            print("line" + str(i) + ": " + line.strip())
            i += 1

except FileNotFoundError:
    print("Error: The 'sample.txt' was not found")
