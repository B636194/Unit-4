file = open("Pitches.txt", "r")
data = file.readlines()
file.close()

for line in data:
    print(line)
